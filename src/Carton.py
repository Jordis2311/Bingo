import random
import math

from bingo import prueba
from bingo import transformar

#Crea un carton de bingo en un formato de 9 filas 3 columnas que no esta garantizado cumplir con el reglamento del juego
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

#Muestra un carton
def imprimirCarton(carton):
    print ("\n")
    for columna in range (0,3):
        for fila in range (0,9):
            print(carton[fila][columna], end = ' ')
        print ("\n")
    print("\n")


#Crea Cartones de bingo hasta que encuentre uno que cumpla con todas las reglamentaciones del bingo y lo devuelve
def generar_carton():
    while True:
        c = intentoCarton()
        n = transformar(c)
        if (prueba(n) == True):
            break
    return c

#Crea y muestra un carton valido
def main():
    imprimirCarton(generar_carton())

if (__name__ == "__main__"):
    main()
