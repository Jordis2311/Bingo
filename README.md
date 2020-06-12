[![Build Status](https://travis-ci.org/Jordis2311/Bingo.svg?branch=master)](https://travis-ci.org/Jordis2311/Bingo)
[![Coverage Status](https://coveralls.io/repos/github/Jordis2311/Bingo/badge.svg?branch=master)](https://coveralls.io/github/Jordis2311/Bingo?branch=master)

Generador de cartones de bingo automatico
Alumno: Jordi Solá

Este repositorio contiene el archivo "Carton.py" dentro de la carpeta src que al ser ejecutado devolvera un carton de bingo valido por pantalla en un formato de 9 filas y 3 columnas.

Esto se logra mediante la funcion genera_carton, la cual ejecuta repetidamente un generador de cartones aleatorio llamado intentoCarton que pasa por una serie de verificaciones de validez que se ejecutan dentro de otra funcion llamada "testeo" hasta encontrar un carton que cumpla con todas las condiciones de validez.

Estas validaciones se encuentra en el archivo "bingo.py", tambien dentro de la carpeta src, donde se encuentran funciones para cada condicion a verificar. A todas estas funciones se les verifica su funcionalidad con la ejecucion de multiples tests ubicados en "test_celdas.py" y "test_1_a_90.py" dentro de la carpeta "tests", estos tests se ejecutan gracias a la funcion pytest, que es utilizada cada vez que se hace un commit en este repositorio

La ejecucion de este codigo puede relentizarse ya que por cuestiones del generador de cartones aleatorios el tiempo de espera a la devolucion del carton es indefinido, ya que se deben generar cartones hasta encontrar uno valido, sin embargo esto no suele tardar mas que unos pocos segundos
