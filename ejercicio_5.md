# Ejercicio 5

**Nombre**: Antonio Joaquín Vitalic Vitalic

---
## Observaciones
Tenga en cuenta las siguientes observaciones al realizar el ejercicio:

- El ejercicio es de carácter **personal**; la copia será penalizada con **nota mínima**.
- De ser necesario investigar, usted esta **autorizado a utilizar internet** como herramienta.
- El uso de modelos generativos de lenguaje como **ChatGPT está estrictamente prohibido** y será penalizado con **nota mínima**. 

## Pregunta 1

HTTP es un protocolo *stateless*, esto significa que no existe ninguna relación entre dos pares (request, response). Esto es particularmente problematico al intentar mantener la coherencia entre una cadena de requests dependientes como por ejemplo el manipular un carrito de compras en un sitio de e-commerce. Como se ha mencionado en clases, una solución para este problema es el uso de **cookies**, las cuales nos permiten mantener un mismo contexto para varias requests. 

Si bien las cookies son muy utiles para mantener una o mas sesiones mientras nos comunicamos con un servidor web, el usarlas o no es una decision moralmente no trivial. En efecto, a lo largo del tiempo el uso de las cookies ha sido cuestionado en numerosas ocasiones.

El objetivo de esta pregunta es que usted investigue las razones por las que el uso de las cookies es controversial y las explique con sus propias palabras.

**Respuesta**: Las cookies son controversiales porque pueden ser usadas para rastrear a los usuarios y sus actividades en la web. Son objeto de debate pues plantean cuestiones de privacidad, debido al almacenamiento de información personal en el navegador del usuario. 

Las cookies pueden ser usadas para almacenar información de inicio de sesión, lo que puede ser un problema de seguridad si un atacante obtiene acceso a las cookies de un usuario. Más aún, las cookies pueden ser usadas para almacenar información de seguimiento de terceros, lo que puede ser un problema de privacidad si un usuario no desea ser rastreado por terceros. Por último, suele no haber claridad con respecto a las políticas de privacidad de las cookies, lo que puede ser un problema de privacidad si un usuario no sabe qué información se está almacenando en su navegador.

## Pregunta 2

Como vimos en el auxiliar, al usar la función **fetch** de Javascript estamos cargando un recurso desde una URL diferente a la que se esta usando. Por esto pueden haber problemas de Cross Origin Request Sharing o **CORS** por sus siglas en inglés.

Investigue y explique qué es CORS. Detalle por qué es importante este mecanismo (**Hint**: Las peticiones AJAX llevan las cookies que se tienen en el sitio objetivo). Nombre una cabecera HTTP de solicitud y una cabecera HTTP de respuesta asociado a este mecanismo.


**Respuesta**: CORS es un mecanismo de seguridad que permite a los navegadores restringir las solicitudes HTTP de origen cruzado (es decir, solicitudes de un dominio a otro). 

Es importante porque permite a los sitios web interactuar con recursos de otros sitios web de forma segura (por ej.: una web que usa una API externa para realizar una acción).

Una cabecera HTTP de solicitud relacionada a CORS es "Origin", mientras que una de respuesta asociada a CORS es "Access-Control-Allow-Origin" (indica si la respuesta puede ser compartida o no por el dominio que lo solicita). Otras solicitudes relacionadas a CORS son "Access-Control-Allow-Credentials" (indica si es que la solicitud puede enviar cookies o no) y "Access-Control-Allow-Methods" (indica qué métodos HTTP están permitidos).
