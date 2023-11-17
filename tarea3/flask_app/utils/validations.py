import re
import filetype

def validate_username(value):
    return value and len(value) > 3 and len(value) < 80


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

def validate_comentarios(comentarios):
    if isinstance(comentarios, str) and len(comentarios) <= 80:
        return True
    else:
        return False

def validate_tipo_artesania(tipo_artesania):
    lista = ["mármol", "madera", "cerámica", "mimbre", "metal", "cuero", "telas", "joyas", "otro"]
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
    if isinstance(nombre, str) and 3 <= len(nombre) <= 80:
        return True
    else:
        return False

def validate_email(email):
    return "@" in email

def validate_celular(celular):
    if isinstance(celular, str) and celular.isdigit() and len(celular) == 9:
        return True
    else:
        return False

def validate_transporte(transporte):
    lista = ["particular", "locomoción pública"]
    return transporte in lista

def validate_deporte(deporte):
    lista = ["Clavados", "Natación", "Natación artística", "Polo acuático", "Natación en Aguas abiertas", "Maratón", "Marcha", "Atletismo", "Bádminton", "Balonmano", "Básquetbol", "Básquetbol 3x3", "Béisbol", "Boxeo", "Bowling", "Breaking", "Canotaje Slalom", "Canotaje de velocidad", "BMX Freestyle", "BMX Racing", "Mountain Bike", "Ciclismo pista", "Ciclismo ruta", "Adiestramiento ecuestre", "Evento completo ecuestre", "Salto ecuestre", "Escalada deportiva", "Esgrima", "Esquí acuático y Wakeboard", "Fútbol", "Gimnasia artística Masculina", "Gimnasia artística Femenina", "Gimnasia rítmica", "Gimnasia trampolín", "Golf", "Hockey césped", "Judo", "Karate", "Levantamiento de pesas", "Lucha", "Patinaje artístico", "Skateboarding", "Patinaje velocidad", "Pelota vasca", "Pentatlón moderno", "Racquetball", "Remo", "Rugby 7", "Sóftbol", "Squash", "Surf", "Taekwondo", "Tenis", "Tenis de mesa", "Tiro", "Tiro con arco", "Triatlón", "Vela", "Vóleibol", "Vóleibol playa"]
    return deporte in lista

def validate_register_artesano(region, comuna, tipo_artesania, descripcion, fotos, nombre, email, celular):
    return validate_region_comuna(region, comuna) and validate_tipo_artesania(tipo_artesania)\
          and validate_descripcion(descripcion) and validate_img(fotos) and \
            validate_nombre(nombre) and validate_email(email) and validate_celular(celular)

def validate_register_hincha(deporte, region, comuna, transporte, nombre, email, celular, comentarios):
    return validate_deporte(deporte) and validate_region_comuna(region, comuna)\
          and validate_transporte(transporte) and validate_nombre(nombre) \
        and validate_email(email) and validate_celular(celular) and validate_comentarios(comentarios)
