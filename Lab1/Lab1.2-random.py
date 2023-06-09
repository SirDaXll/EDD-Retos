import random

# Funcion para crear una matriz aleatoria
def matriz_random(filas, columnas):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elem = random.randint(1, 5) # Numero aleatorio entre 1 y 5
            fila.append(elem)
        m.append(elem)
    return m

# Resta de 2 matrices
def resta_matrices(m1, m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])): # El [0] es para indicar que recorra la lista m1 de nuevo desde la posicion 0
            resta = m1[i][j] - m2[i][j]
            fila.append(resta)
        matriz_final.append(fila)
    return matriz_final

# Suma de 2 matrices
def resta_matrices(m1, m2):
    matriz_final = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])): # El [0] es para indicar que recorra la lista m1 de nuevo desde la posicion 0
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        matriz_final.append(fila)
    return matriz_final

# Se crean 2 matrices random de un mismo tamaño
filas = int(input('Ingrese la cantidad de filas de la matriz: '))
columnas = int(input('Ingrese la cantidad de columnas de la matriz: '))
print('Creando la primera matriz aleatoria:')
m1 = matriz_random(filas, columnas)
print(m1,'\n')
print('Creando la segunda matriz aleatoria:')
m2 = matriz_random(filas, columnas)
print(m2,'\n')

#