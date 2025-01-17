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
	cursor.execute("SELECT LAST_INSERT_ID();")
	conn.commit()
	artesano_id = cursor.fetchone()
	return artesano_id

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

def get_comuna_by_comuna_id(comuna_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_by_comuna_id"], (comuna_id,))
	comuna = cursor.fetchone()
	return comuna

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

def get_region_by_comuna_id(comuna_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_region_by_comuna_id"], (comuna_id,))
	region_id = cursor.fetchone()
	cursor.execute(QUERY_DICT["get_region_by_region_id"], (region_id,))
	region_nombre = cursor.fetchone()
	return region_nombre

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

def get_artesano_by_id(artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_artesano_by_id"], (artesano_id,))
	artesano = cursor.fetchone()
	return artesano

def insertar_hincha(comuna_id, modo_transporte, nombre, email, celular, comentarios):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_hincha"], (comuna_id, modo_transporte, nombre, email, celular, comentarios))
	cursor.execute("SELECT LAST_INSERT_ID();")
	conn.commit()
	hincha_id = cursor.fetchone()
	return hincha_id

def get_hincha_by_id(hincha_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_hincha_by_id"], (hincha_id,))
	hincha = cursor.fetchone()
	return hincha

def get_deporte_id_by_deporte(deporte):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_deporte_id_by_deporte"], (deporte,))
	deporte_id = cursor.fetchone()
	return deporte_id

def insertar_hincha_deporte(hincha_id, deporte_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_hincha_deporte"], (hincha_id, deporte_id))
	conn.commit()

def obtener_deportes_de_hincha_particular(hincha_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_deportes_de_hincha_particular"], (hincha_id))
	deporte = cursor.fetchone()
	return deporte

def get_modo_transporte_de_hincha_particular(hincha_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_modo_transporte_de_hincha_particular"], (hincha_id,))
	modo_transporte = cursor.fetchone()
	return modo_transporte

def get_celular_de_hincha_particular(hincha_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_celular_de_hincha_particular"], (hincha_id,))
	celular = cursor.fetchone()
	return celular

def get_hinchas_by_page_prev_next(pag_prev, pag_next):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_hinchas_by_page_prev_next"], (pag_prev, pag_next))
	hinchas = cursor.fetchall()
	return hinchas

def obtener_datos_artesania():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT tipo_artesania.nombre, COUNT(artesano_tipo.artesano_id) AS total \
				FROM tipo_artesania LEFT JOIN artesano_tipo \
				ON tipo_artesania.id = artesano_tipo.tipo_artesania_id \
				GROUP BY tipo_artesania.nombre")
	data = cursor.fetchall()
	return data

def obtener_datos_deporte():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("SELECT deporte.nombre, COUNT(hincha_deporte.hincha_id) AS total \
				FROM deporte LEFT JOIN hincha_deporte \
				ON deporte.id = hincha_deporte.deporte_id \
				GROUP BY deporte.nombre")
	data = cursor.fetchall()
	return data

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

