import random
import math

from bingo import validar_quince_celdas
from bingo import validar_no_mayor_quince
from bingo import validar_no_menor_quince
from bingo import todas_columnas_con_numeros
from bingo import todas_filas_con_numeros
from bingo import incremento_columna
from bingo import incremento_fila
from bingo import no_repite_elementos
from bingo import columnas_no_completas
from bingo import cinco_celdas_por_fila
from bingo import dos_celdas_ocupadas
from bingo import dos_celdas_vacias
from bingo import matrix_tres_nueve
from bingo import tres_columna_una

def intentoCarton():
    contador = 0

    carton = [
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0],
      [0,0,0]
    ]

    numeroscarton = 0

    while (numeroscarton < 15):
        contador += 1
        if (contador == 50):
            return intentoCarton()

        numero = random.randint(1,90)

        columna = math.floor(numero / 10)
        if (columna == 9):
            columna = 8
        
        huecos = 0
        for i in range (0,3):
            if (carton[columna][i] == 0):
                huecos += 1
            if (carton[columna][i] == numero):
                huecos = 0
                break
        if (huecos < 2):
            continue

        fila = 0
        for j in range (0,3):
            huecos = 0
            for i in range (0,9):
                if (carton[i][fila] == 0):
                    huecos += 1
            
            if (huecos < 5 or carton[columna][fila] != 0):
                fila += 1
            else:
                break
        
        if (fila == 3):
            continue
        
        carton[columna][fila] = numero
        numeroscarton += 1
        contador = 0
    
    for x in range (0,9):
        huecos = 0
        for y in range (0,3):
            if (carton[x][y] == 0):
                huecos += 1
        if (huecos == 3):
            return intentoCarton()

    return carton

def imprimirCarton(carton):
    print ("\n")
    for columna in range (0,3):
        for fila in range (0,9):
            print(carton[fila][columna], end = ' ')
        print ("\n")
    print("\n")

def transformar(carton):
    nuevo = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]
    for i in range (0,3):
        for x in range (0,9):
            nuevo[i][x] = carton[x][i]
    return nuevo

def testeo(c):
    res = True
    if(validar_quince_celdas(c) != True):
        res = False
        return res
    if(validar_no_mayor_quince(c) != True):
        res = False
        return res
    if(validar_no_menor_quince(c) != True):
        res = False
        return res
    if(todas_columnas_con_numeros(c) != True):
        res = False
        return res
    if(todas_filas_con_numeros(c) != True):
        res = False
        return res
    if(incremento_columna(c) != True):
        res = False
        return res
    if(incremento_fila(c) != True):
        res = False
        return res
    if(no_repite_elementos(c) != True):
        res = False
        return res
    if(columnas_no_completas(c) != True):
        res = False
        return res
    if(cinco_celdas_por_fila(c) != True):
        res = False
        return res
    if(dos_celdas_ocupadas(c) != True):
        res = False
        return res
    if(dos_celdas_vacias(c) != True):
        res = False
        return res
    if(matrix_tres_nueve(c) != True):
        res = False
        return res
    if(tres_columna_una(c) != True):
        res = False
        return res
    return res

def generar_carton():
    while True:
        c = intentoCarton()
        n = transformar(c)
        if (testeo(n) == True):
            break
    return c

def main():
    imprimirCarton(generar_carton())

if (__name__ == "__main__"):
    main()
