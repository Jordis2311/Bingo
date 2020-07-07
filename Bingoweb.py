from jinja2 import Template
from src.bingo import generar_carton

template = Template(open("web/plantilla.jinja2").read())

file = open("Bingo.html", "w")
file.write(template.render(carton = generar_carton()))
file.close()
print("Creando \"Bingo.html\".")