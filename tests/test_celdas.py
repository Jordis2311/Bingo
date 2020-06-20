from src.bingo import columna
from src.bingo import validar_quince_celdas
from src.bingo import validar_no_mayor_quince
from src.bingo import validar_no_menor_quince
from src.bingo import todas_columnas_con_numeros
from src.bingo import todas_filas_con_numeros
from src.bingo import incremento_columna
from src.bingo import incremento_fila
from src.bingo import no_repite_elementos
from src.bingo import columnas_no_completas
from src.bingo import cinco_celdas_por_fila
from src.bingo import dos_celdas_ocupadas
from src.bingo import dos_celdas_vacias
from src.bingo import matrix_tres_nueve
from src.bingo import tres_columna_una
from src.bingo import uno_a_noventa
from src.bingo import prueba
from src.bingo import transformar
from src.bingo import intentoCarton
from src.bingo import generar_carton
from src.bingo import imprimirCarton


#Revisar si la funcion que valida que el carton tiene 15 celdas ocupadas funciona correctamente
def test_celdas_15():
    mi_carton = (
     (1,0,0,1,1,0,1,1,0),
     (0,1,0,0,0,1,1,0,1),
     (1,0,1,1,1,0,1,1,0)
    )
    assert validar_quince_celdas(mi_carton) == True
    mi_carton = (
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0)
    )
    assert validar_quince_celdas(mi_carton) == False
    

#Revisar si la funcion que valida que el carton tiene maximo 15 celdas ocupadas funciona correctamente
def test_celdas_no_mayor_15():
    mi_carton = (
     (1,0,0,1,1,0,1,1,0),
     (0,1,0,0,0,1,1,0,1),
     (0,1,1,1,1,0,1,1,0)
    )
    assert validar_no_mayor_quince(mi_carton) == True
    mi_carton = (
    (1,1,1,1,1,1,1,1,1),
    (1,1,1,1,1,1,1,1,1),
    (1,1,1,1,1,1,1,1,1)
    )
    assert validar_no_mayor_quince(mi_carton) == False

#Revisar si la funcion que valida que el carton tiene minimo 15 celdas ocupadas funciona correctamente
def test_celdas_no_menor_15():
    mi_carton = (
     (1,0,0,1,1,1,0,1,0),
     (1,0,0,0,0,1,1,0,1),
     (0,1,1,1,1,0,1,0,1)
    )
    assert validar_no_menor_quince(mi_carton) == True
    mi_carton = (
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0)
    )
    assert validar_no_menor_quince(mi_carton) == False

#Revisa si la funcion que valida que cada columna tiene al menos 1 celda ocupada funciona correctamente
def test_columna_carton():
    mi_carton = (
     (1,0,1,1,0,1,0,1,0),
     (1,0,0,0,0,1,1,0,1),
     (0,1,1,1,1,0,0,1,1)
    )
    assert todas_columnas_con_numeros(mi_carton) == True
    mi_carton = (
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0)
    )
    assert todas_columnas_con_numeros(mi_carton) == False

#Revisa si la funcion que revisa que las celdas de un bingo no esten completas funciona correctamente
def test_celda_completa():
    mi_carton = (
     (1,0,1,1,0,1,0,1,0),
     (1,0,0,0,0,1,1,0,1),
     (0,1,1,1,1,0,0,1,1)
    )
    assert columnas_no_completas(mi_carton) == True
    mi_carton = (
    (1,1,1,1,1,1,1,1,1),
    (1,1,1,1,1,1,1,1,1),
    (1,1,1,1,1,1,1,1,1)
    )
    assert columnas_no_completas(mi_carton) == False


#Revisa si la funcion que valida que cada fila tiene al menos 1 celda ocupada funciona correctamente
def test_fila_carton():
    mi_carton = (
     (1,1,0,1,0,1,0,1,0),
     (1,0,1,0,1,0,1,0,1),
     (0,1,0,1,1,0,0,1,1)
    )
    assert todas_filas_con_numeros(mi_carton) == True
    mi_carton = (
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0)
    )
    assert todas_filas_con_numeros(mi_carton) == False


#Revisa si la funcion incremento columna funciona correctamente
def test_incremento_columnas():
    mi_carton = (
    (1,11,0,31,0,0,61,0,81),
    (0,0,22,0,42,52,62,72,0),
    (3,13,0,33,43,0,0,0,83)
    )
    assert incremento_columna(mi_carton) == True
    mi_carton = (
    (90,0,65,0,49,33,22,17,0),
    (87,72,0,56,0,0,0,10,1),
    (0,0,64,55,0,31,20,0,0)
    )
    assert incremento_columna(mi_carton) == False

#Revisa si la funcion incremento filas funciona correctamente
def test_incremento_filas():
    mi_carton = (
    (1,11,0,31,0,0,61,0,81),
    (0,0,22,0,42,52,62,72,0),
    (3,13,0,33,43,0,0,0,83)
    )
    assert incremento_fila(mi_carton) == True
    mi_carton = (
    (90,0,65,0,49,33,22,17,0),
    (87,72,0,56,0,0,0,10,1),
    (0,0,64,55,0,31,20,0,0)
    )
    assert incremento_fila(mi_carton) == False

#Revisa si la funcion que verifica que el carton no repite elementos esta bien
def test_repite_elemento():
    mi_carton = (
    (1,11,0,31,0,0,61,0,81),
    (0,0,22,0,42,52,62,72,0),
    (3,13,0,33,43,0,0,0,83)
    )
    assert no_repite_elementos(mi_carton) == True
    mi_carton = (
    (90,0,90,0,90,0,90,90,0),
    (90,90,0,90,0,90,0,90,90),
    (0,0,90,90,0,90,90,0,0)
    )
    assert no_repite_elementos(mi_carton) == False

#Verifica que la funcion cinco celdas por fila esta bien
def test_cinco_fila():
    mi_carton = (
    (1,1,0,1,0,0,1,0,1),
    (0,0,1,0,1,1,1,1,0),
    (1,1,0,1,1,0,0,0,1)
    )
    assert cinco_celdas_por_fila(mi_carton) == True
    mi_carton = (
    (0,90,90,0,90,90,90,90,0),
    (90,90,0,90,0,90,0,90,90),
    (0,90,90,90,0,90,90,90,0)
    )
    assert cinco_celdas_por_fila(mi_carton) == False

#Verifica que la funcion que revisa si un carton tiene cumple con la condicion de celdas ocupadas seguidas
def test_celdas_ocupadas_seguidas():
    mi_carton = (
    (1,1,0,1,0,0,1,0,1),
    (0,0,1,0,1,1,0,1,0),
    (1,1,0,1,1,0,1,0,1)
    )
    assert dos_celdas_ocupadas(mi_carton) == True
    mi_carton = (
    (1,1,1,1,1,0,1,0,1),
    (0,1,1,1,1,1,0,1,0),
    (1,1,0,1,1,1,1,0,1)
    )
    assert dos_celdas_ocupadas(mi_carton) == False


#Verifica que la funcion que revisa si un carton tiene cumple con la condicion de celdas vacias seguidas
def test_celdas_vacias_seguidas():
    mi_carton = (
    (1,1,0,1,0,0,1,0,1),
    (0,0,1,0,1,1,0,1,0),
    (1,1,0,1,1,0,1,0,1)
    )
    assert dos_celdas_vacias(mi_carton) == True
    mi_carton = (
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0)
    )
    assert dos_celdas_vacias(mi_carton) == False

def test_matrix():
    mi_carton = (
    (1,1,0,1,0,0,1,0,1),
    (0,0,1,0,1,1,0,1,0),
    (1,1,0,1,1,0,1,0,1)
    )
    assert matrix_tres_nueve(mi_carton) == True
    mi_carton = (
    (1,1,0,1,0,0,1,0),  
    (0,0,1,0,1,1,0,1),
    )
    assert matrix_tres_nueve(mi_carton) == False

def test_tres_columnas():
    mi_carton = (
    (1,11,0,31,0,0,61,0,81),
    (0,0,22,0,42,52,0,72,0),
    (3,13,0,33,43,0,62,0,83)
    )
    assert tres_columna_una(mi_carton) == True
    mi_carton = (
    (1,11,0,31,41,0,61,0,81),
    (0,0,22,0,42,52,0,72,0),
    (3,13,0,33,43,0,62,0,0)
    )
    assert tres_columna_una(mi_carton) == False

def test_uno_a_noventa():
    mi_carton = (
    (1,11,0,31,0,0,61,0,81),
    (0,0,22,0,42,52,0,72,0),
    (3,13,0,33,43,0,62,0,83)
    )
    assert uno_a_noventa(mi_carton) == True
    mi_carton = (
    (-10,11,0,31,41,0,61,0,202),
    (0,0,22,0,42,99,0,72,0),
    (3,13,0,-45,43,0,62,0,33)
    )
    assert uno_a_noventa(mi_carton) == False

def test_testeo():
    mi_carton = (
    (0,0,23,32,0,56,0,72,80),
    (0,10,28,0,0,58,0,79,82),
    (7,11,0,39,41,0,60,0,0)
    )
    assert prueba(mi_carton) == True
    mi_carton = (
    (-10,11,0,31,41,0,61,0,202),
    (0,0,22,0,42,99,0,72,0),
    (3,13,0,-45,43,0,62,0,33)
    )
    assert prueba(mi_carton) == False

def test_tranformar():
    mi_carton = [
      [1,0,0],
      [0,1,0],
      [0,0,1],
      [0,1,0],
      [1,0,0],
      [0,1,0],
      [0,0,1],
      [0,1,0],
      [1,0,0]
    ]
    nuevo = transformar(mi_carton)
    for i in range (0,3):
        for x in range (0,9):
            assert nuevo[i][x] == mi_carton[x][i]

def test_intento():
    carton = intentoCarton()
    n = transformar(carton)
    assert matrix_tres_nueve(n) == True

def test_generador():
    carton = generar_carton()
    assert prueba(carton) == True