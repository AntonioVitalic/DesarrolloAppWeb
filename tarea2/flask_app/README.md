# Tarea 2

**Nombre**: Antonio Joaquín Vitalic Vitalic

Usé un virtual enviroment con Python 3.12.0. En el archivo requirements.txt están los paquetes que usé. Para instalarlos, se debe usar el comando `pip install -r requirements.txt` dentro del virtual enviroment. Usé Flask 3.0.0, no creo que haya problemas con versiones anteriores, mostradas en las auxiliares (justo se liberó una versión nueva estas última semana) pero no lo probé.

Se usó MySQL y Beekeeper Studio para la base de datos. El archivo [tarea2.sql](/tarea2/flask_app/database/tarea2.sql) contiene el código para crear la base de datos y las tablas. El archivo [region-comuna.sql](/tarea2/flask_app/database/region-comuna.sql) contiene el código para insertar los datos de regiones y comunas. El archivo [sentencias.sql](/tarea2/flask_app/database/sentencias.sql) contiene las querys sugeridas en la tarea, y las que usé en con pymysql, están en el archivo [querys.json](/tarea2/flask_app/database/querys.json). Las descripciones de las querys tanto en [querys.json](/tarea2/flask_app/database/querys.json) como en [db.py](/tarea2/flask_app/database/db.py) son literales (en esp. o ing.) de las sentencias, por facilidad.

Con respecto al archivo [registrar_hincha.html](/tarea2/flask_app/templates/sistema_jjpp/registrar_hincha.html) y [registrar_artesano.html](/tarea2/flask_app/templates/sistema_jjpp/registrar_artesano.html), se usó lo mostrado [aquí](https://github.com/habibmhamadi/multi-select-tag) para el multiselect de deporte y tipo de artesanía, respectivamente.

Con respecto a la selección de comuna dependiendo de la región seleccionada, se usó un código del profesor, mostrado [aquí](https://codepen.io/jourzua/pen/NWeNYow?externo=1). Se dan créditos al profesor, y a [@juanbrujo](https://gist.github.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd) por los arrays con strings de comunas.

Con respecto al archivo [styles.css](/tarea2/flask_app/static/css/styles.css), me inspiré en el contenido del tag style que se usa [aquí](https://www.w3schools.com/css/tryit.asp?filename=trycss_navbar_horizontal_black).

Todos los archivos .html cumplen con el validador de HTML http://validator.w3.org/ (salvo por un par de warnings, pero ningún error). El archivo styles.css cumple con el validador de CSS https://jigsaw.w3.org/css-validator/#validate_by_upload.