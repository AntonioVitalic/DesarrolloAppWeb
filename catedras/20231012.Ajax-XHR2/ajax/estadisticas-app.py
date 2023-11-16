from flask import Flask, make_response, render_template
import pymysql
import pymysql.cursors
import time
import datetime
  
app = Flask(__name__)
  
@app.route('/datos-pais', methods = ['GET'])
def datos_pais():
    # obtener información
    c = getConnection()
    datos = get_datos_pais(c)
    resp = make_response(datos)
    resp.headers["Content-type"] = "application/json;charset=UTF-8"
    resp.headers["Cache-Control"] = "no-cache"
    return resp

@app.route('/datos-visitas', methods = ['GET'])
def datos_visitas():
    # obtener información
    c = getConnection()
    datos = get_visitas_dia(c)
    resp = make_response(datos)
    resp.headers["Content-type"] = "application/json;charset=UTF-8"
    resp.headers["Cache-Control"] = "no-cache"
    return resp

@app.route('/pais', methods = ['GET'])
def index():
    return render_template('pais.html')

@app.route('/visitas', methods = ['GET'])
def visitas():
    return render_template('visitas.html')

def getConnection():
    conv = pymysql.converters.conversions.copy()
    conv[10]=str

    conn = pymysql.connect(
    db='ejemplo',
    user='cc5002',
    passwd='cc5002',
    host='localhost',
    charset='utf8',
    conv=conv)
    return conn

def get_datos_pais(c):
    sql = "SELECT pais, total FROM visitas";
    cursor = c.cursor()
    cursor.execute(sql)
    c.commit()
    datos = cursor.fetchall()
    texto = "["
    for d in datos:
        texto = texto + "[\"" + d[0] + "\"," + str(d[1]) + "],"
    texto = texto[:-1]
    texto = texto + "]"
    return texto

def get_visitas_dia(c):
    sql = "SELECT dia, total FROM visitas_dia";
    cursor = c.cursor()
    cursor.execute(sql)
    c.commit()
    datos = cursor.fetchall()
    texto = "["
    for d in datos:
        formated_date = datetime.datetime.strptime(d[0],"%Y-%m-%d")
        Unix_timestamp = datetime.datetime.timestamp(formated_date)
        texto = texto + "[" + str(Unix_timestamp*1000) + "," + str(d[1]) + "],"
    texto = texto[:-1]
    texto = texto + "]"
    return texto
  
app.run(debug=True)


