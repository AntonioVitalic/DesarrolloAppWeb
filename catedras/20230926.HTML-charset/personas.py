#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import pymysql

print("Content-type: text/html; charset=UTF-8")
#print("Content-type: text/html; charset=ISO-8859-1")
print("")

# conexion a base de datos
conn = pymysql.connect(
    db='ejemplo',
    user='cc5002',
    passwd='cc5002',
    host='localhost',
    charset='utf8')
c = conn.cursor()

# revisar si nos hicieron submit
mensaje = ""
datos = cgi.FieldStorage()
if len(datos) > 0:
    # insertar
    sql = "INSERT INTO persona (nombre, apellido) VALUES (%s, %s)"
    try:
        resultado = c.execute(sql, (datos['nombre'].value, datos['apellido'].value))
        conn.commit()
        if resultado == 1:
            mensaje = "insertada nueva persona: " +\
                       datos['nombre'].value + " " +\
                       datos['apellido'].value
        else:
            mensaje = "error, no se insertó persona en la base de datos"
    except pymysql.Error as e:
        mensaje = "Error con base de datos: {0} {1} ".format(e.args[0], e.args[1])

# mostrar HTML
print("""
<!DOCTYPE html>
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Ejemplo Python con Base Datos</title>
 </head>
 <body>
 <h1>Ejemplo Python con Base Datos</h1>
""")
if mensaje != "":
    print("<p>", mensaje, "</p>")

# obtenemos las personas desde la base de datos
sql = "SELECT id, nombre, apellido FROM persona";
c.execute(sql)
conn.commit()
personas = c.fetchall()

if len(personas) > 0:
    print("<table border=1>")
    print("<tr><td><b>ID</b></td>\
               <td><b>Nombre</b></td>\
               <td><b>Apellido</b></td></tr>")
    for p in personas:
        print("<tr><td>", p[0], "</td><td>", p[1], "</td><td>", p[2], "</td></tr>")

    print("</table>")

# cerramos recursos usados para interactuar con la base de datos
c.close()
conn.close()

print("""
<h2> Ingreso de nueva persona: </h2>
<form action="personas.py" method="post">
Nombre   <input type="text" name="nombre" /><br />
Apellido   <input type="text" name="apellido" /><br />
<input type="submit" value=" > agregar persona " />
</form>
</body></html>
""")
