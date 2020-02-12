![Python version](https://img.shields.io/badge/python-%5E3.7-yellow.svg)
![Flask version](https://img.shields.io/badge/flask-%5E1.0-blue.svg)
![SQL Alchemy version](https://img.shields.io/badge/flask--sqlalchemy-%5E2.4-blue.svg)

# Extracción y procesamiento de datos a partir de historiales clínicos de pacientes

Repositorio para el *Trabajo de Fin de Grado* (TFG) del alumno *Omar Mendo Mesa* para el grado de Ingeniería Informática
de la Universidad de La Laguna (ULL).

El proyecto se basa principalmente en la extracción y procesamiento de datos de historiales clínicos de pacientes de
un centro especializado en neurología a partir de la información contenida en archivos con el historial clínico. Además, 
he querido realizar una mejora al proyecto, creando una aplicación web con **Flask** (framework de desarrollo web para Python),
la cual servirá de herramienta de consulta de los historiales clínicos de forma más sencilla, clara y eficiente.

También, se ha diseñado una sección en la aplicación para el estudio estadístico que se ha realizado con los datos obtenidos
extraídos de los historiales clínicos, creando un ambiente de carácter de investigación para muestrear de forma
gráfica los datos de los pacientes, ya sea de manera individual o colectiva, para que el equipo médico pueda visualizar
diferentes contrastes y alteraciones en las medidas del test [CAMDEX](http://web.teaediciones.com/camdex-rprueba-de-exploracion-cambridge-revisada-para-la-valoracion-de-los-trastornos-mentales-en-la-vejez.aspx),
y poder ver el impacto de los diversos tratamientos que se pueden aplicar sobre el paciente y ver su comportamiento
en el tiempo gráficamente.

## Tecnologías utilizadas
*   [Python](https://www.python.org/)
*   [Flask](http://flask.pocoo.org/)
*   [Git](https://git-scm.com/)
*   [Javascript](https://www.javascript.com/)
*   [SQLite](https://www.sqlite.org/index.html)
*   [HTML/CSS (BootStrap v4)](https://getbootstrap.com/)
*   [DataTables](https://datatables.net/)
*   [Plotly.js](https://plot.ly/javascript/)

## Secciones principales del proyecto
*Extract-py* está desarrollado íntegramente en **[Flask](http://flask.pocoo.org/)**, uno de los framework de desarrollo web
más populares para *Python*
* Nada más entrar a la aplicación web desarrollada, tenemos una página de inicio de sesión para los especialistas del centro
médico.

![Inicio](/extract/static/img/pic1.png "Pantalla de inicio")

* A continuación, tenemos un formulario de login y otro de registro, ya que necesitamos tener un control de usuarios debido
al carácter sensible de los datos usados en la aplicación.

![Login](/extract/static/img/pic2.png "Formulario de login")

* Una vez hemos accedido a la plataforma, tenemos distintas tablas con información relevante al paciente seleccionado: una
con sus datos personales (superior) y otra con las distintas mediciones realizadas en las múltiples sesiones del examen CAMDEX-R 
del paciente.

![Tablas](/extract/static/img/pic3.png "Tablas de datos")

* Además, en esta sección tenemos un CRUD para la gestión de los usuarios del sistema.

![CRUD](/extract/static/img/pic4.png "CRUD de gestión de usuarios")

* Por último, tenemos la sección más interesante, que es la de visualización de los datos mediante gráficas, desarroladas con *Plotly*,
con el fin de que tanto el especialista como el paciente/familiares puedas comprender la mejoría/empeoramiento de los resultados
obtenidos en las diferentes pruebas del examen CAMDEX-R a lo largo del tiempo (pinchando en la imagen, se accede a un vídeo de YouTube).

[![Visualización](/extract/static/img/pic5.png)](https://youtu.be/qUaQWQHkdAc "Visualización")

## Memoria del proyecto

Para acceder a la memoria del proyecto, acceda a este [link](https://riull.ull.es/xmlui/handle/915/16587).


#### Contacto

*   Universidad de La Laguna - ESIT
*   Alumno: [Omar Mendo Mesa](https://github.com/beejeke)
*   Tutor: Carlos Pérez González