import numpy
import random

filas = int(input('Ingrese la cantidad de filas de la matriz: '))
columnas = int(input('Ingrese la cantidad de columnas de la matriz: '))
escalar = int(input('Ingrese el escalar que multiplicará la matriz: '))

# Ingreso de elementos Matriz
print('Ingresando los elementos de la matriz...')
# Crear matriz con solo ceros
m = numpy.zeros((filas,columnas))
for i in range(filas):
    for j in range(columnas):
        elem = random.randint(0,10)
        m[i][j] = elem
print('La matriz generada es:\n',m)