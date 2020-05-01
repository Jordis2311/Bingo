from src.bingo import carton
from src.bingo import columna
from src.bingo import validar_quince_celdas


#Revisar si el carton tiene 15 celdas ocupadas
def test_celdas_15():
    mi_carton = carton()
    assert validar_quince_celdas(mi_carton) == True

#Revisar si el carton tiene maximo 15 celdas ocupadas
def test_celdas_no_mayor_15():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    
    assert contador <= 15

#Revisar si el carton tiene minimo 15 celdas ocupadas
def test_celdas_no_menor_15():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    
    assert contador >= 15 

#Revisa si cada columna tiene al menos 1 celda ocupada
def test_columna_carton():
    mi_carton = carton()
    res = True
    for i in range (0,9):
        ct = 0
        (celda1,celda2,celda3) = columna(mi_carton,i)
        ct = ct + celda1 + celda2 + celda3
        if (ct == 0):
            res = False
    assert res == True

#Revias si cada fila tiene al menos 1 celda ocupada
def test_fila_carton():
    mi_carton = carton()
    res = True
    for fila in mi_carton:
        ct = 0
        for celda in fila:
            ct = ct + celda
        if (ct == 0):
            res = False
    assert res == True
