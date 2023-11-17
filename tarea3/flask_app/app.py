from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_cors import cross_origin
from utils.validations import validate_login_user, validate_register_user, validate_register_artesano, validate_register_hincha
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from datetime import datetime, timedelta
import random

UPLOAD_FOLDER = 'static/uploads'

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
        deportes = request.form.get("deportes")
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        transporte = request.form.get("transporte")
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        celular = request.form.get("celular")
        comentarios = request.form.get("comentarios")
        print("request.method == POST: deportes:", deportes)
        print("request.method == POST: region:", region)
        print("request.method == POST: comuna:", comuna)
        print("request.method == POST: transporte:", transporte)
        print("request.method == POST: nombre:", nombre)
        print("request.method == POST: email:", email)
        print("request.method == POST: celular:", celular)
        print("request.method == POST: comentarios:", comentarios)

        if validate_register_hincha(deportes, region, comuna, transporte, nombre, email, celular, comentarios):

            # 1. obtenemos la comuna_id a partir de la comuna,
            # esto porque no se guarda la comuna directamente en la tabla hincha
            comuna_id = db.get_comuna_id_by_comuna(comuna)
            print("hincha comuna_id:", comuna_id)

            # 2. guardamos hincha en la base de datos, y obtenemos el id del hincha con SELECT LAST_INSERT_ID()
            hincha_id = db.insertar_hincha(comuna_id, transporte, nombre, email, celular, comentarios)

            print("hincha_id:", hincha_id)

            # 4. guardamos el deporte en la base de datos
            db.insertar_hincha_deporte(hincha_id, deportes)
        
    return render_template("index.html")

@app.route("/registrar_artesano", methods=["GET", "POST"])
def registrar_artesano():

    if request.method == "GET":
        return render_template("registrar_artesano.html")
    
    if request.method == "POST":
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        tipo_artesania = request.form.get("tipo-artesania")
        descripcion = request.form.get("descripcion-artesania")
        fotos = request.files.get("fotos-artesania")
        nombre = request.form.get("nombre-artesano")
        email = request.form.get("email-artesano")
        celular = request.form.get("celular-artesano")
        print("request.method == POST: region:", region)
        print("request.method == POST: comuna:", comuna)
        print("request.method == POST: tipo_artesania:", tipo_artesania)
        print("request.method == POST: descripcion:", descripcion)
        print("request.method == POST: fotos:", fotos)
        print("request.method == POST: nombre:", nombre)
        print("request.method == POST: email:", email)
        print("request.method == POST: celular:", celular)

        if validate_register_artesano(region, comuna, tipo_artesania, descripcion, fotos, nombre, email, celular):
            # 1. generamos un nombre random para la imagen
            _filename = hashlib.sha256(
                secure_filename(fotos.filename).encode("utf-8")
                ).hexdigest()
            _extension = filetype.guess(fotos).extension
            img_filename = f"{_filename}.{_extension}"

            # 2. guardamos imagen
            fotos.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

            # 3. obtenemos la comuna_id a partir de la comuna,
            # esto porque no se guarda la comuna directamente en la tabla artesano
            comuna_id = db.get_comuna_id_by_comuna(comuna)

            # 4. guardamos artesano en la base de datos
            artesano_id = db.insertar_artesano(comuna_id, descripcion, nombre, email, celular)

            print("artesano_id:", artesano_id)

            # 5. insertar_artesano_tipo(artesano_id, tipo_artesania_id)
            tipo_artesania_id = db.get_tipo_artesania_id_by_tipo_artesania(tipo_artesania)
            print("tipo_artesania_id:", tipo_artesania_id)
            db.insertar_artesano_tipo(artesano_id, tipo_artesania_id)

            # 6. insertar_foto(ruta_archivo, nombre_archivo, artesano_id)
            db.insertar_foto(app.config["UPLOAD_FOLDER"], img_filename, artesano_id)
            
    return render_template("index.html")


@app.route("/ver_hinchas/<int:num>", methods=["GET", "POST"])
def ver_hinchas(num):
    data = []
    pageinfo = {}
    if num <= 1:
        pageinfo["prev"] = False
        pageinfo["next"] = True
        data = db.get_hinchas_by_page_prev_next(0, 5)
    else:
        pageinfo["prev"] = True
        data = db.get_hinchas_by_page_prev_next((num-1)*5, 10)
        if len(data) < 5:
            pageinfo["next"] = False
        else:
            pageinfo["next"] = True
    
    hincha_id, comuna_nombre, modo_transporte, hincha_nombre, email, celular, comentarios = data

    # obtenermos deportes de hincha
    deportes = db.obtener_deportes_de_hincha_particular(hincha_id)

    final_data = [hincha_nombre, comuna_nombre, deportes, modo_transporte, celular]

    return render_template("ver_hinchas.html", data=final_data, pageinfo=pageinfo)

@app.route("/ver_artesanos/<int:num>", methods=["GET", "POST"])
def ver_artesanos(num):
    # Ver Listado de Artesanos: debe obtener el listado de artesanos registrados en la base
    # de datos y los debe desplegar tal como se indicó en la tarea 1. Se deben mostrar en
    # grupos de 5 filas, si hay más de 5 artesanos registrados en la base de datos, los debe
    # mostrar por página permitiendo avanzar y retroceder según corresponda

    # get artesanos by page (5 artesanos por página)
    data = []
    pageinfo = {}
    if num <= 1:
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

    artesano_id, comuna_nombre, descripcion_artesania, artesano_nombre, email, celular = data

    # obtenermos tipos_artesania de artesano
    tipo_artesania = db.obtener_tipos_artesania_de_artesano_particular(artesano_id)

    # obtenemos fotos informadas por artesano
    fotos = db.obtener_fotos_informadas_por_artesano(artesano_id)

    final_data = [artesano_nombre, celular, comuna_nombre, tipo_artesania, fotos]

    return render_template("ver_artesanos.html", data=final_data, pageinfo=pageinfo)

@app.route("/informacion_hincha", methods=["GET", "POST"])
def informacion_hincha(id):
    return render_template("informacion_hincha.html")

@app.route("/informacion_artesano", methods=["GET", "POST"])
def informacion_artesano(id):
    return render_template("informacion_artesano.html")


@app.route('/datos_estadisticas')
def datos_estadisticas():
    # Obtener los datos de la base de datos
    datos = db.obtener_datos()

    datos_artesanos = datos["artesanos"]
    datos_hinchas = datos["hinchas"]

    # Devolver los datos como una respuesta JSON
    return jsonify({
        'artesanos': datos_artesanos,
        'hinchas': datos_hinchas
    })

@app.route("/estadisticas", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def estadisticas():
   # Obtén los datos desde la base de datos
    datos = db.obtener_datos()

    datos_artesanos = datos["artesanos"]
    datos_hinchas = datos["hinchas"]

    return render_template("estadisticas.html", artesanos=datos_artesanos, hinchas=datos_hinchas)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
