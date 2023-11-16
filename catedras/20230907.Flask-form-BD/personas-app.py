from flask import Flask
from flask import request, render_template
from persona import Persona
import pymysql

app = Flask(__name__)

@app.route('/personas', methods=['POST', 'GET'])
def personas():
    error = None
    personas = None
    mensaje = None
    c = getConnection()
    if request.method == 'POST':
        if (agrega_persona(c, request.form['nombre'], request.form['apellido'])):
            mensaje = "Agregada nueva persona " + request.form['nombre'] + " " + request.form['apellido']
        else:
            error = 'No se pudo agregar persona'
    personas = get_personas(c)
    return render_template('personas.html', mensaje=mensaje, error=error, personas=personas)

def agrega_persona(c, nombre, apellido):
    if not nombre or not apellido:
        return False
    sql = "INSERT INTO persona (nombre, apellido) VALUES (%s, %s)"
    try:
        resultado = c.cursor().execute(sql, (nombre, apellido))
        c.commit()
        return resultado == 1
    except pymysql.Error as e:
        app.logger.error("Error con base de datos: {0} {1} ".format(e.args[0], e.args[1]))
    return False

def getConnection():
    conn = pymysql.connect(
    db='ejemplo',
    user='cc5002',
    passwd='cc5002',
    host='localhost',
    charset='utf8')
    return conn

def get_personas(c):
    sql = "SELECT id, nombre, apellido FROM persona";
    cursor = c.cursor()
    cursor.execute(sql)
    c.commit()
    personas = cursor.fetchall()
    listaPersonas = []
    if len(personas) > 0:
        for per in personas:
            personaBD = Persona(per[0], per[1], per[2])
            listaPersonas.append(personaBD)
    return listaPersonas

if __name__ == "__main__":
    app.run(debug=True)
