import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('database/querys.json', 'r') as querys:
	QUERY_DICT = json.load(querys)

# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

# -- querys --

def get_user_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_user_by_id"], (id,))
	user = cursor.fetchone()
	return user

def get_user_by_email(email):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_user_by_email"], (email,))
	user = cursor.fetchone()
	return user

def get_user_by_username(username):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_user_by_username"], (username,))
	user = cursor.fetchone()
	return user

def create_user(username, password, email):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_user"], (username, password, email))
	conn.commit()

def insertar_artesano(comuna_id, descripcion_artesania, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_artesano"], (comuna_id, descripcion_artesania, nombre, email, celular))
	conn.commit()

def obtener_list_artesano_desde_mas_reciente(artesano):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_list_artesano_desde_mas_reciente"], (artesano))
	artesano = cursor.fetchone()
	return artesano

def obtener_list_artesano_desde_mas_reciente_limitado_primeros_5(artesano):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_list_artesano_desde_mas_reciente_limitado_primeros_5"], (artesano))
	artesano = cursor.fetchone()
	return artesano

def get_comuna_id_by_comuna(comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_id_by_comuna"], (comuna,))
	comuna_id = cursor.fetchone()
	return comuna_id

def get_artesanos_by_page_prev_next(pag_prev, pag_next):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_artesanos_by_page_prev_next"], (pag_prev, pag_next))
	artesanos = cursor.fetchall()
	return artesanos

def obtener_list_artesano_desde_mas_reciente_limitado_siguientes_5(username, password, email):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_list_artesano_desde_mas_reciente_limitado_siguientes_5"], (username, password, email))
	artesano = cursor.fetchone()
	return artesano

def obtener_list_artesano_con_nombre_comuna_en_lugar_de_ID(artesano, comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_list_artesano_con_nombre_comuna_en_lugar_de_ID"], (artesano, comuna))
	artesano = cursor.fetchone()
	return artesano

def insertar_artesano_tipo(artesano_id, tipo_artesania_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_artesano_tipo"], (artesano_id, tipo_artesania_id))
	conn.commit()

def get_tipo_artesania_id_by_tipo_artesania(tipo_artesania):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_tipo_artesania_id_by_tipo_artesania"], (tipo_artesania,))
	tipo_artesania_id = cursor.fetchone()
	return tipo_artesania_id
	
def obtener_tipos_artesania_de_artesano_particular(artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_tipos_artesania_de_artesano_particular"], (artesano_id))
	tipo_artesania = cursor.fetchone()
	return tipo_artesania

def insertar_foto(ruta_archivo, nombre_archivo, artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_foto"], (ruta_archivo, nombre_archivo, artesano_id))
	conn.commit()

def obtener_fotos_informadas_por_artesano(artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_fotos_informadas_por_artesano"], (artesano_id))
	foto = cursor.fetchone()
	return foto

def obtener_el_ultimo_id_insertado():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_el_ultimo_id_insertado"])
	id = cursor.fetchone()
	return id


def insertar_hincha(comuna_id, modo_transporte, nombre, email, celular, comentarios):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_hincha"], (comuna_id, modo_transporte, nombre, email, celular, comentarios))
	conn.commit()
	# Obtener el ID del hincha recién insertado
	hincha_id = obtener_el_ultimo_id_insertado()
	# con el hincha_id, insertar los deportes

def insertar_hincha_deporte():
	pass

def obtener_datos():
    conn = get_conn()
    cursor = conn.cursor()

    # Obtener datos de artesanos
    cursor.execute("SELECT id FROM artesano")
    resultados_artesanos = cursor.fetchall()
    datos_artesanos = [resultado[0] for resultado in resultados_artesanos]

    # Obtener datos de hinchas
    cursor.execute("SELECT nombre FROM hincha")
    resultados_hinchas = cursor.fetchall()
    datos_hinchas = [resultado[0] for resultado in resultados_hinchas]

    conn.close()

    datos = {
        'artesanos': datos_artesanos,
        'hinchas': datos_hinchas
    }

    return datos

# -- db-related functions --

def register_user(username, password, email):
	# 1. check the email is not in use
	_email_user = get_user_by_email(email)
	if _email_user is not None:
		return False, "El correo ya esta en uso."
	# 2. check the username is not in use
	_username_user = get_user_by_username(username)
	if _username_user is not None:
		return False, "El nombre de usuario esta en uso."
	# 3. create user
	create_user(username, password, email)
	return True, None

def login_user(username, password):
	a_user = get_user_by_username(username)
	if a_user is None:
		return False, "Usuario o contraseña incorrectos."

	a_user_passwd = a_user[3]
	if a_user_passwd != password:
		return False, "Usuario o contraseña incorrectos."
	return True, None

