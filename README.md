[![Build Status](https://travis-ci.org/Jordis2311/Bingo.svg?branch=master)](https://travis-ci.org/Jordis2311/Bingo)
[![Coverage Status](https://coveralls.io/repos/github/Jordis2311/Bingo/badge.svg?branch=master)](https://coveralls.io/github/Jordis2311/Bingo?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Jordis2311/Bingo/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Jordis2311/Bingo/?branch=master)
# Generador de cartones de bingo
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

# Descargar
Para clonar mi repositorio ingresa en tu terminal

```https://github.com/Jordis2311/Bingo.git```

Para utilizar este repositorio es necesario tener instalador Python, pip y Jinja2

Link de la pagina de `Python`:

```https://www.python.org/downloads/```

Guia de como Instalar `pip`:

```https://www.liquidweb.com/kb/install-pip-windows/```

Para instalar `jinja2`:

```pip install jinja2```

Para distribuciones basadas en Debian utilizar `pip3`

# Uso
Para generar un carton:

```python src/bingo.py```

Ejemplo:
```
$ python3 src/bingo.py
2  0  20 0  0  54 0  74 82

8  0  27 34 0  56 0  79 0

0  18 0  39 41 0  65 0  83
```

Para generar un html del carton:

```python Bingoweb.py```

Ejemplo:

Generado "bingo.html".

![Ejemplo Bingo Web](https://github.com/Jordis2311/Bingo/blob/master/Ejemplo%20Carton.PNG?raw=true)

# Licencia
Este repositorio esta bajo la licencia GNU GLP v3, para más informacion leer dicha licencia
