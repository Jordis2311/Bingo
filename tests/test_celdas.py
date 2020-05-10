from src.bingo import carton
from src.bingo import columna
from src.bingo import validar_quince_celdas
from src.bingo import validar_no_mayor_quince
from src.bingo import validar_no_menor_quince
from src.bingo import todas_columnas_con_numeros
from src.bingo import todas_filas_con_numeros
from src.bingo import incremento_columna
from src.bingo import incremento_fila
from src.bingo import no_repite_elementos

#Revisar si la funcion que valida que el carton tiene 15 celdas ocupadas funciona correctamente
def test_celdas_15():
    mi_carton = (
     (1,0,0,1,1,0,1,1,0),
     (0,1,0,0,0,1,1,0,1),
     (1,0,1,1,1,0,1,1,0)
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

#Revisa si la funcion que valida que cada fila tiene al menos 1 celda ocupada funciona correctamente
def test_fila_carton():
    mi_carton = (
     (1,1,0,1,0,1,0,1,0),
     (1,0,1,0,1,0,1,0,1),
     (0,1,0,1,1,0,0,1,1)
    )
    assert todas_filas_con_numeros(mi_carton) == True

#Revisa si la funcion incremento columna funciona correctamente
def test_incremento_columnas():
    mi_carton = (
    (1,11,0,31,0,0,61,0,81),
    (0,0,22,0,42,52,62,72,0),
    (3,13,0,33,43,0,0,0,83)
    )
    assert incremento_columna(mi_carton) == True

#Revisa si la funcion incremento filas funciona correctamente
def test_incremento_filas():
    mi_carton = (
    (1,11,0,31,0,0,61,0,81),
    (0,0,22,0,42,52,62,72,0),
    (3,13,0,33,43,0,0,0,83)
    )
    assert incremento_fila(mi_carton) == True

#Revisa si la funcion que verifica que el carton no repite elementos esta bien
def test_repite_elemento():
    mi_carton = (
    (1,11,0,31,0,0,61,0,81),
    (0,0,22,0,42,52,62,72,0),
    (3,13,0,33,43,0,0,0,83)
    )
    assert no_repite_elementos(mi_carton) == True