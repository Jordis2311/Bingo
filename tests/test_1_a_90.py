from src.bingo import carton
from src.bingo import columna

#Revisar si el carton tiene 15 celdas ocupadas
def test_unoanoventa():
    mi_carton = carton()
    contador = 0

    for fila in range(0, 3):
        for columna in range (0,9):
            celda = mi_carton[fila][columna]
            assert celda >= 0 and celda <=90