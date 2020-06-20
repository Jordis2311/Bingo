import random
import math

# Los 0 son celdas vacias

#Devuelve una columna del carton
def columna(carton, nro_columna):
    return(
        carton[0][nro_columna],
        carton[1][nro_columna],
        carton[2][nro_columna]
    )

#Revisar si el carton tiene 15 celdas ocupadas
def validar_quince_celdas(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                contador = contador + 1
    return contador == 15

#Revisar si el carton tiene maximo 15 celdas ocupadas
def validar_no_mayor_quince(carton):
    contador = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                contador = contador + 1
    return contador <= 15

#Revisar si el carton tiene minimo 15 celdas ocupadas
def validar_no_menor_quince(carton):
    contador = 0
    for fila in carton:
      for celda in fila:
          if celda != 0:
            contador = contador + 1
    return contador >= 15

#Revisa si cada columna tiene al menos 1 celda ocupada
def todas_columnas_con_numeros(carton):
    res = True
    for i in range (0,9):
        (c1,c2,c3) = columna(carton,i)
        if(c1 == 0 and c2 == 0 and c3 == 0):
            res = False
    return res == True

#Revisa que una columna no tenga las 3 celdas ocupadas
def columnas_no_completas(carton):
    res = True
    for i in range (0,9):
        (c1,c2,c3) = columna(carton,i)
        if(c1 != 0 and c2 != 0 and c3 != 0):
            res = False
    return res == True

#Revisa si cada fila tiene al menos 1 celda ocupada
def todas_filas_con_numeros(carton):
    res = True
    for fila in carton:
        ct = 0
        for celda in fila:
            ct = ct + celda
        if (ct == 0):
            res = False
    return res == True

#Revisar si en una columna los numeros menores estan por encima de los mayores
def incremento_columna(carton):
    res = True
    for i in range (0,9):
        (celda1,celda2,celda3) = columna(carton,i)
        if (celda1 > celda2 and celda2 != 0) or (celda1 > celda3 and celda3 != 0):
            res = False
        if (celda2 > celda3 &celda3 != 0):
            res = False
    return res == True


#Revisar si en una columna los numeros menores estan a la izquierda de los mayores
def incremento_fila(carton):
    res = True
    for fila in carton:
        for i in range (0,9):
            for x in range (i+1,9):
                if (fila[i] > fila[x] and fila[x] != 0 and fila[i] != 0):
                    res = False
    return res == True 

#Revisa si el carton no tiene elementos repetidos
def no_repite_elementos(carton):
    numeros = []
    res = True
    for fila in carton:
        for celda in fila:
            numeros.append(celda)
            if (numeros.count(celda) > 1 and celda != 0):
                res = False
    return res == True

#Verifica que haya 5 celdas ocupadas por fila
def cinco_celdas_por_fila(carton):
    res = True
    for fila in carton:
        cant = 0
        for celda in fila:
            if (celda != 0):
                cant += 1
        if(cant != 5):
            res = False
    return res == True


#Verifica que el carton no tenga mas de 2 celdas ocupadas seguidas
def dos_celdas_ocupadas(carton):
    res = True
    for fila in carton:
        cc = 0
        for celda in fila:
            if (celda != 0):
                cc +=1
            else:
                cc = 0
            if (cc > 2):
                res = False
    return res == True

#Verifica que el carton no tenga mas de 2 celdas vacias seguidas
def dos_celdas_vacias(carton):
    res = True
    for fila in carton:
        cc = 0
        for celda in fila:
            if (celda == 0):
                cc +=1
            else:
                cc = 0
            if (cc > 2):
                res = False
    return res == True

#Verifica que el carton sea una matrix de 3 x 9
def matrix_tres_nueve(carton):
    res = True
    cantc = 0
    for fila in carton:
        cantc += 1
        cantf = len(fila)
        if (cantf != 9):
            res = False
    if (cantc != 3):
        res = False
    return res == True  

#Verifica que el carton tenga 3 y solo 3 columnas con una celda ocupada
def tres_columna_una(carton):
    res = True
    cn = 0
    for i in range (0,9):
        (c1,c2,c3) = columna(carton,i)
        ct = 0
        if (c1 != 0):
            ct += 1
        if (c2 != 0):
            ct += 1
        if (c3 != 0):
            ct += 1
        if (ct == 1):
            cn += 1
    if (cn != 3):
        res = False
    return res == True

#Revisar si los numeros del carton estan entre 1 y 90
def uno_a_noventa(mi_carton):
    res = True
    for fila in range(0, 3):
        for columna in range (0,9):
            celda = mi_carton[fila][columna]
            if (celda < 0 or celda > 90):
                res = False
    return res == True

#Verifica que el carton cumpla con todas las reglamentaciones del bingo
def prueba(carton):
    res = True
    if((validar_quince_celdas(carton) != True) or (validar_no_mayor_quince(carton) != True) or (validar_no_menor_quince(carton) != True) or (todas_columnas_con_numeros(carton) != True)
    or (todas_filas_con_numeros(carton) != True) or (incremento_columna(carton) != True) or (incremento_fila(carton) != True) or (no_repite_elementos(carton) != True)
    or (columnas_no_completas(carton) != True) or (cinco_celdas_por_fila(carton) != True) or (dos_celdas_ocupadas(carton) != True) or (dos_celdas_vacias(carton) != True)
    or (matrix_tres_nueve(carton) != True) or (tres_columna_una(carton) != True) or (uno_a_noventa(carton) != True)):
        res = False
    return res

#Cambia el formato de un carton a el formato usado en las validaciones de cartones
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
