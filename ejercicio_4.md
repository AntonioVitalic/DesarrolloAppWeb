# Ejercicio 4: "*Unrestricted File Upload*"

**Nombre**: Antonio Joaquín Vitalic Vitalic

--- 
## Introducción
Hemos enfatizado la importancia de ser extremadamente cautelosos en el manejo de la entrada de los usuarios, incluyendo los archivos. De hecho, la vulnerabilidad [*Unrestricted File Upload*](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload), la cual corresponde a confiar plenamente en los archivos subidos por el usuario, puede tener consecuencias catastróficas.

El objetivo de este ejercicio es comprender bien las posibles **consecuencias** de un manejo de archivos "mediocre" y las formas de **prevenirlas**.

## Pregunta 1
Investigue y explique **con sus propias palabras** 3 posibles ataques que un usuario malicioso podria realizar a una aplicación web con la vulnerabilidad *Unrestricted File Upload*". Se espera que para cada ataque se mencionen las **consecuencias** del mismo.

**Respuesta:** Los posibles ataques son:

1. Malware: El usuario malicioso sube un archivo malicioso al servidor, como un virus, el cual puede comprometer al sistema y a los usuarios que lo usan.

2. Sobreescritura de archivos: Un atacante puede aprovechar el escaso manejo de almacenamiento de archivos para sobreescribir archivos del sistema, como por ejemplo el archivo de configuración de la base de datos, lo cual puede comprometer la integridad de los datos y el funcionamiento del sistema en sí.

3. Remote Code Execution (RCE): Un usuario malicioso puede subir un archivo que contenga un script (el cual puede ser ejecutado por el servidor), con el cual el atacante podrá, por ejemplo, robar datos del servidor, modificar o apagar el sistema.

## Pregunta 2
Ahora que ya tenemos claro que descuidar el manejo de archivos es peligroso, les pedimos listar 5 métodos preventivos para esta vulnerabilidad.

**Respuesta:** Los métodos preventivos son:

1. Sistema de permisos. No todos los usuarios deberían poder subir archivos, y no todos los archivos deberian ser accesibles para todos los usuarios.

2. Validar el tipo de archivo que se sube. Si el archivo no es del tipo esperado, no se debe subir. Por ejemplo, si se espera un archivo de imagen, no se debe subir un archivo con extensión .js.

3. Validar el contenido. Si bien un archivo a priori puede ser del tipo esperado, puede contener código malicioso. Por ejemplo, un archivo de imagen puede contener código malicioso en su metadata.

4. Incorporar un sistema adecuado de renombramiento de archivos. Esto evita que un atacante pueda robar un archivo importante con un nombre típico y fácil de obtener, para esto se puede usar la fecha de subida del archivo, o un hash del contenido.

5. Incorporar un límite de tamaño de archivo. Esto evita que un atacante pueda subir un archivo muy grande y ocupar todo el espacio de almacenamiento del servidor.