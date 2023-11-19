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
        # obtengamos los datos de deportes, los cuales son multiple
        deportes = request.form.getlist("deportes")
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

            # 3. obtenemos el deporte_id a partir del deporte,
            # esto porque no se guarda el deporte directamente en la tabla hincha

            for deporte in deportes:
                deporte_id = db.get_deporte_id_by_deporte(deporte)
                print("deporte_id:", deporte_id)

                # 4. guardamos el deporte en la base de datos
                db.insertar_hincha_deporte(hincha_id, deporte_id)
            msg = "Hincha registrado exitosamente!"
        
    return render_template("index.html", msg=msg)

@app.route("/registrar_artesano", methods=["GET", "POST"])
def registrar_artesano():

    if request.method == "GET":
        return render_template("registrar_artesano.html")
    
    if request.method == "POST":
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        tipos_artesanias = request.form.getlist("tipo-artesania")
        descripcion = request.form.get("descripcion-artesania")
        fotos = request.files.get("fotos-artesania")
        nombre = request.form.get("nombre-artesano")
        email = request.form.get("email-artesano")
        celular = request.form.get("celular-artesano")

        if validate_register_artesano(region, comuna, tipos_artesanias, descripcion, fotos, nombre, email, celular):
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

            # print("artesano_id:", artesano_id)

            # 5. insertar_artesano_tipo(artesano_id, tipo_artesania_id)
            for tipo_artesania in tipos_artesanias:
                tipo_artesania_id = db.get_tipo_artesania_id_by_tipo_artesania(tipo_artesania)
                # print("tipo_artesania_id:", tipo_artesania_id)
                db.insertar_artesano_tipo(artesano_id, tipo_artesania_id)

            # 6. insertar_foto(ruta_archivo, nombre_archivo, artesano_id)
            db.insertar_foto(app.config["UPLOAD_FOLDER"], img_filename, artesano_id)
            msg = "Artesano registrado exitosamente!"
            
    return render_template("index.html", msg=msg)


@app.route("/ver_hinchas/<int:num>", methods=["GET", "POST"])
def ver_hinchas(num):
    pageinfo = {}
    if num <= 1:
        pageinfo["prev"] = False
        pageinfo["next"] = True
        hinchas = db.get_hinchas_by_page_prev_next(0, 5)
    else:
        pageinfo["prev"] = True
        hinchas = db.get_hinchas_by_page_prev_next((num-1)*5, 10)
        if len(hinchas) < 5:
            pageinfo["next"] = False
        else:
            pageinfo["next"] = True
    
    data = []
    for hincha in hinchas:
        hincha_id, comuna_nombre, modo_transporte, hincha_nombre, email, celular, comentarios = hincha

        # obtenermos deportes de hincha
        deportes = db.obtener_deportes_de_hincha_particular(hincha_id)

        data.append({"hincha_id": hincha_id,
                     "hincha_nombre": hincha_nombre,
                     "comuna_nombre": comuna_nombre,
                     "deportes": deportes,
                     "modo_transporte": modo_transporte,
                     "celular": celular,
                    })

    return render_template("ver_hinchas.html", data=data, pageinfo=pageinfo)

@app.route("/ver_artesanos/<int:num>", methods=["GET", "POST"])
def ver_artesanos(num):
    # Ver Listado de Artesanos: debe obtener el listado de artesanos registrados en la base
    # de datos y los debe desplegar tal como se indicó en la tarea 1. Se deben mostrar en
    # grupos de 5 filas, si hay más de 5 artesanos registrados en la base de datos, los debe
    # mostrar por página permitiendo avanzar y retroceder según corresponda

    # get artesanos by page (5 artesanos por página)
    pageinfo = {}
    if num <= 1:
        pageinfo["prev"] = False
        pageinfo["next"] = True
        artesanos = db.get_artesanos_by_page_prev_next(0, 5)
    else:
        pageinfo["prev"] = True
        artesanos = db.get_artesanos_by_page_prev_next((num-1)*5, 10)
        if len(artesanos) < 5:
            pageinfo["next"] = False
        else:
            pageinfo["next"] = True

    data = []
    for artesano in artesanos:
        artesano_id, comuna_nombre, descripcion_artesania, artesano_nombre, email, celular = artesano

        # obtenermos tipos_artesanias de artesano
        tipos_artesanias = db.obtener_tipos_artesania_de_artesano_particular(artesano_id)
        # print("tipos_artesanias:", tipos_artesanias)

        # obtenemos fotos informadas por artesano
        fotos = db.obtener_fotos_informadas_por_artesano(artesano_id)

        img_filename =  f"/{fotos[0]}/{fotos[1]}"

        data.append({"artesano_id": artesano_id,
                     "artesano_nombre": artesano_nombre,
                     "celular": celular,
                     "comuna_nombre": comuna_nombre,
                     "tipo_artesania": tipos_artesanias,
                     "path_image": img_filename,
                    })

    return render_template("ver_artesanos.html", data=data, pageinfo=pageinfo)

@app.route("/informacion_hincha/<int:id>", methods=["GET", "POST"])
def informacion_hincha(id):
    # obtenemos la fila de la tabla hincha, cuya llave primaria es id
    hincha = db.get_hincha_by_id(id)

    hincha_id, comuna_id, modo_transporte, nombre, email, celular, comentarios = hincha

    # obtenemos la comuna de hincha
    comuna_nombre = db.get_comuna_by_comuna_id(comuna_id)

    # obtenemos los deportes de hincha
    deportes = db.obtener_deportes_de_hincha_particular(hincha_id)

    # obtenemos la region de hincha
    region_nombre = db.get_region_by_comuna_id(comuna_id)

    data = {"hincha_nombre": nombre,
            "celular": celular,
            "comuna_nombre": comuna_nombre,
            "region_nombre": region_nombre,
            "email": email,
            "modo_transporte": modo_transporte,
            "deportes": deportes,
            "comentarios": comentarios
            }
    
    return render_template("informacion_hincha.html", data=data)


@app.route("/informacion_artesano/<int:id>", methods=["GET"])
def informacion_artesano(id):
    # Obtener los datos del artesano con el ID proporcionado
    artesano = db.get_artesano_by_id(id)
    artesano_id, comuna_id, descripcion_artesania, nombre, email, celular = artesano

    # Obtener la comuna del artesano
    comuna_nombre = db.get_comuna_by_comuna_id(comuna_id)

    # Obtener los tipos de artesanía del artesano
    tipo_artesania = db.obtener_tipos_artesania_de_artesano_particular(artesano_id)

    # Obtener las fotos informadas por el artesano
    fotos = db.obtener_fotos_informadas_por_artesano(artesano_id)
    img_filename = f"/{fotos[0]}/{fotos[1]}"

    # Obtener la región del artesano
    region_nombre = db.get_region_by_comuna_id(comuna_id)

    data = {
        "artesano_nombre": nombre,
        "celular": celular,
        "comuna_nombre": comuna_nombre,
        "region_nombre": region_nombre,
        "email": email,
        "tipo_artesania": tipo_artesania,
        "path_image": img_filename,
        "descripcion_artesania": descripcion_artesania
    }

    return render_template("informacion_artesano.html", data=data)


@app.route('/estadisticas', methods=["GET"])
def estadisticas():
    return render_template("estadisticas.html")

@app.route("/get-stats-data", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_stats_data():
    data_artesania = db.obtener_datos_artesania()
    data_deporte = db.obtener_datos_deporte()

    nombres_tipos_artesania = [row[0] for row in data_artesania]
    frecuencias_tipos_artesania = [row[1] for row in data_artesania]

    nombres_deportes = [row[0] for row in data_deporte]
    frecuencias_deportes = [row[1] for row in data_deporte]

    return jsonify({"nombres_tipos_artesania": nombres_tipos_artesania,
                    "frecuencias_tipos_artesania": frecuencias_tipos_artesania,
                    "nombres_deportes": nombres_deportes,
                    "frecuencias_deportes": frecuencias_deportes})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
