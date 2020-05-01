
# Los 0 son celdas vacias
# Los 1 son celdas Ocupadas
def carton():
    carton = (
        (1,1,0,1,0,1,0,1,1),
        (1,0,1,0,1,0,1,0,0),
        (0,1,1,0,0,1,0,1,1)
    )
    return carton

def columna(carton, nro_columna):
    return(
        carton[0][nro_columna],
        carton[1][nro_columna],
        carton[2][nro_columna]
    )

def validar_quince_celdas(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                contador = contador + 1
    return contador == 15