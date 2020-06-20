[![Build Status](https://travis-ci.org/Jordis2311/Bingo.svg?branch=master)](https://travis-ci.org/Jordis2311/Bingo)[![Coverage Status](https://coveralls.io/repos/github/Jordis2311/Bingo/badge.svg)](https://coveralls.io/github/Jordis2311/Bingo)

# Generaodor de cartones de bingo
Proyecto para la materia de AAT de 6to Año Informatica del Instituto Politecnico Superior
Alumno: Jordi Solá
Profesor: Mariano Dagostino

# Bingo
Este juego consiste en la reparticion de un carton de bingo a cada jugador el cual contiene una matrix de 3x9 con 15 numeros que van aumentando hacia abajo e izquierda en el rango de 1 a 90
Luego se sacara aleatoriamente una ficha que contenga un numero de ese rango y los jugadores que la tienen ese numero dentro del carton deben marcarlo en el.
El jugador que primero consiga completar una fila del carton sera el ganador

# Descripcion del Repositorio

Mi generador de cartones de bingo esta estructurado de la siguiente manera:
la funcion que genera el codigo y todas las validaciones de condiciones del carton estan incluidas en el archivo bingo.py dentro de la carpeta src.
Para obtener un carton lo que se debe hacer es ejecutar el archivo bingo.py, este devolvera en consola un carton de bingo que se podra utilizar para el juego.
Las funciones de este repositorio pasan un proceso de comprobacion para regular que esten funcionando correctamente por las funciones "test" ubicadas todas en el archivo "test_celdas" dentro de la carpeta "tests" esta verificacion de funcionamiento es realizada cada vez que se realiza un cambio en el repositorio gracias a Travis CI el ejecuta el comando pytest en dichos momentos
