
# Los 0 son celdas vacias
# Los 1 son celdas Ocupadas

#Define un carton
def carton():
    carton = (
        (1,1,0,1,0,1,0,1,1),
        (1,0,1,0,1,0,1,0,0),
        (0,1,1,0,0,1,0,1,1)
    )
    return carton

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