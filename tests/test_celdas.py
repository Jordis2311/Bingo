from src.bingo import carton
from src.bingo import columna
from src.bingo import validar_quince_celdas
from src.bingo import validar_no_mayor_quince
from src.bingo import validar_no_menor_quince
from src.bingo import todas_columnas_con_numeros
from src.bingo import todas_filas_con_numeros

#Revisar si la funcion que valida que el carton tiene 15 celdas ocupadas funciona correctamente
def test_celdas_15():
    mi_carton = (
     (1,0,0,1,1,0,1,1,0),
     (0,1,0,0,0,1,1,0,1),
     (0,0,1,1,1,0,1,1,0)
    )
    assert validar_quince_celdas(mi_carton) == True

#Revisar si la funcion que valida que el carton tiene maximo 15 celdas ocupadas funciona correctamente
def test_celdas_no_mayor_15():
    mi_carton = (
     (1,0,0,1,1,0,1,1,0),
     (0,1,0,0,0,1,1,0,1),
     (0,1,1,1,1,0,1,1,0)
    )
    assert validar_no_mayor_quince(mi_carton) == True

#Revisar si la funcion que valida que el carton tiene minimo 15 celdas ocupadas funciona correctamente
def test_celdas_no_menor_15():
    mi_carton = (
     (1,0,0,1,1,1,0,1,0),
     (1,0,0,0,0,1,1,0,1),
     (0,1,1,1,1,0,1,0,1)
    )
    assert validar_no_menor_quince(mi_carton) == True

#Revisa si la funcion que valida que cada columna tiene al menos 1 celda ocupada funciona correctamente
def test_columna_carton():
    mi_carton = (
     (1,0,1,1,0,1,0,1,0),
     (1,0,0,0,0,1,1,0,1),
     (0,1,1,1,1,0,0,1,1)
    )
    assert todas_columnas_con_numeros(mi_carton) == True

#Revias si la funcion que valida que cada fila tiene al menos 1 celda ocupada funciona correctamente
def test_fila_carton():
    mi_carton = (
     (1,1,0,1,0,1,0,1,0),
     (1,0,1,0,1,0,1,0,1),
     (0,1,0,1,1,0,0,1,1)
    )
    assert todas_filas_con_numeros(mi_carton) == True
