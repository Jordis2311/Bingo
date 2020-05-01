from src.bingo import carton
from src.bingo import columna

#Revisar si los numeros del carton estan entre 1 y 90
def test_unoanoventa():
    mi_carton = carton()
    for fila in range(0, 3):
        for columna in range (0,9):
            celda = mi_carton[fila][columna]
            assert celda >= 0 and celda <=90