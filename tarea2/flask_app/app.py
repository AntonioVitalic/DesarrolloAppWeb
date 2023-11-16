from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import validate_login_user, validate_register_user, validate_register_artesano, validate_register_hincha
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os

UPLOAD_FOLDER = 'tarea2/flask_app/static/uploads'

app = Flask(__name__, template_folder='templates/sistema_jjpp')


app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# --- Routes ---
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/registrar_hincha", methods=["GET", "POST"])
def registrar_hincha():

    if request.method == "GET":
        return render_template("registrar_hincha.html")

    if request.method == "POST":
        deporte = request.form.get("deporte")
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        transporte = request.form.get("transporte")
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        celular = request.form.get("celular")
        comentarios = request.form.get("comentarios")

        if validate_register_hincha(deporte, region, comuna, transporte, nombre, email, celular, comentarios):
            # 1. save confession in db
            db.create_hincha(deporte, region, comuna, transporte, nombre, email, celular, comentarios)
        
    return render_template("registrar_hincha.html")

@app.route("/registrar_artesano", methods=["GET", "POST"])
def registrar_artesano():

    if request.method == "GET":
        return render_template("registrar_artesano.html")
    
    if request.method == "POST":
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        tipo_artesania = request.form.get("tipo-artesania")
        descripcion = request.form.get("descripcion-artesania")
        fotos = request.form.get("fotos-artesania")
        nombre = request.form.get("nombre-artesano")
        email = request.form.get("email-artesano")
        celular = request.form.get("celular-artesano")

        if validate_register_artesano(region, comuna, tipo_artesania, descripcion, fotos, nombre, email, celular):
            # 1. generate random name for img
            _filename = hashlib.sha256(
                secure_filename(fotos.filename).encode("utf-8")
                ).hexdigest()
            _extension = filetype.guess(fotos).extension
            img_filename = f"{_filename}.{_extension}"

            # 2. save img as a file
            fotos.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

            # 3. save insert artesano form in db with db.insertar_artesano(comuna_id, descripcion_artesania, nombre, email, celular)
            comuna_id = db.get_comuna_id_by_comuna(comuna)
            db.insertar_artesano(comuna_id, descripcion, nombre, email, celular)
    
    return redirect(url_for("index"))

@app.route("/ver_hinchas", methods=["GET", "POST"])
def ver_hinchas():
    # siguiente tarea
    return render_template("ver_hinchas.html")

@app.route("/ver_artesanos/<int:n>", methods=["GET", "POST"])
def ver_artesanos(num):
    data = []
    pageinfo = {}
    if num == 1:
        pageinfo["prev"] = False
        pageinfo["next"] = True
        data = db.get_artesanos_by_page_prev_next(0, 5)
    else:
        pageinfo["prev"] = True
        data = db.get_artesanos_by_page_prev_next((num-1)*5, 10)
        if len(data) < 5:
            pageinfo["next"] = False
        else:
            pageinfo["next"] = True

    return render_template("ver_artesanos.html", data=data, pageinfo=pageinfo)

@app.route("/informacion_hincha", methods=["GET", "POST"])
def informacion_hincha(id):
    return render_template("informacion_hincha.html")

@app.route("/informacion_artesano", methods=["GET", "POST"])
def informacion_artesano(id):
    return render_template("informacion_artesano.html")

if __name__ == "__main__":
    app.run(debug=True)
