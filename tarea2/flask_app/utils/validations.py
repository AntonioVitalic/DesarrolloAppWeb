import re
import filetype

def validate_username(value):
    return value and len(value) > 4


def validate_password(value):
    malas = ["1234", "admin1", "odio a mis Aux >:(2"]
    return bool(re.search(r"\d", value)) and not value in malas


def validate_email(value):
    return "@" in value


def validate_login_user(username, password):
    return validate_username(username) and validate_password(password)


def validate_register_user(username, password, email):
    return validate_username(username) and validate_password(password) and validate_email(email)



def validate_conf_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if conf_img is None:
        return False

    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True


def validate_region_comuna(region, comuna):
    return True

def validate_tipo_artesania(tipo_artesania):
    lista = ["Mármol", "Madera", "Cerámica", "Mimbre", "Metal", "Cuero", "Telas", "Joyas", "Otro tipo"]
    return tipo_artesania in lista

def validate_descripcion(descripcion):
    return True

def validate_img(fotos):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if fotos is None:
        return False

    # check if the browser submitted an empty file
    if fotos.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(fotos)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validate_nombre(nombre):
    return nombre and len(nombre) > 4

def validate_email(email):
    return "@" in email

def validate_celular(celular):
    return celular and len(celular) == 9

def validate_register_artesano(region, comuna, tipo_artesania, descripcion, fotos, nombre, email, celular):
    return validate_region_comuna(region, comuna) and validate_tipo_artesania(tipo_artesania) and validate_descripcion(descripcion) and validate_img(fotos) and validate_nombre(nombre) and validate_email(email) and validate_celular(celular)

def validate_register_hincha(deporte, region, comuna, transporte, nombre, email, celular, comentarios):
    return True
