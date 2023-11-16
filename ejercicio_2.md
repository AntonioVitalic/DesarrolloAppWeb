# Ejercicio 2
**Nombre**: Antonio Joaquin Vitalic Vitalic

---

## Observaciones
Tenga en cuenta las siguientes observaciones al realizar el ejercicio:

- El ejercicio es de carácter **personal**; la copia será penalizada con **nota mínima**.
- De ser necesario investigar, usted esta **autorizado a utilizar internet** como herramienta.
- El uso de modelos generativos de lenguaje como **ChatGPT está estrictamente prohibido** y será penalizado con **nota mínima**. 

## Pregunta 1

¿Qué es el ataque de "Cross-Site Scripting" (XSS) y cómo podría prevenirse en el desarrollo front-end? Describa un escenario en el cual este tipo de ataque podría ser especialmente peligroso.

**Respuesta**: El ataque de "Cross-Site Scripting" (XSS) es un tipo de ataque que se produce cuando un atacante inserta código malicioso en una página web, con el fin de que cuando un usuario visite la página, el código se ejecute en su navegador. El código malicioso puede ser de cualquier tipo, pero el más común es JavaScript. El ataque XSS puede ser especialmente peligroso cuando el atacante puede obtener acceso a la información confidencial del usuario, como contraseñas, números de tarjetas de crédito, etc. 

Para prevenir el ataque XSS en el desarrollo front-end, se debe:
- Validar la entrada de datos del usuario, para asegurarse de que no contenga código malicioso.

- Escapar correctamente los datos de salida, hay que ingresar los datos ingresados como texto plano, para que el navegador no los interprete como código.

- Utilizar el encabezado de seguridad HTTP "Content-Security-Policy" para evitar que se cargue código malicioso en la página web.

- Mantener software actualizado con las últimas versiones de seguridad.

## Pregunta 2
Existen variadas librerías y *frameworks* de Javascript que se pueden utilizar para programar tareas más complejas en el Frontend y manipular el DOM con mayor facilidad. Investigue, nombre y describa 3 de las librerías o Frameworks de javascript más usados en el desarrollo web (por ejemplo, **JQuery**). Si tuviese que implementar su página web ¿Cuál utilizaría?   

**Respuesta**: Las librerías o frameworks de javascript más usados en el desarrollo web son: 

- ReactJs: es una librería Javascript de código abierto diseñada para crear interfaces de usuario con el objetivo de facilitar el desarrollo de aplicaciones en una sola página. Es mantenido por Facebook y la comunidad de software libre

- Angular: es un framework para aplicaciones web desarrollado en TypeScript, de código abierto, mantenido por Google, que se utiliza para crear y mantener aplicaciones web de una sola página.

- Vue.js:  es un framework de JavaScript de código abierto para la construcción de interfaces de usuario y aplicaciones de una sola página. 