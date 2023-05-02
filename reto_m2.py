# Multiplicación de Matriz por escalar
import numpy
import random

filas = int(input('Ingrese la cantidad de filas de la matriz: '))
columnas = int(input('Ingrese la cantidad de columnas de la matriz: '))
while True:
    try:
        escalar = int(input('Ingrese el escalar entero que multiplicará la matriz: '))
        break
    except ValueError:
        print('El valor ingresado no es un número entero. Intente nuevamente.')

# Ingreso de elementos Matriz
print('Ingresando los elementos de la matriz...')
# Crear matriz con solo ceros
m = numpy.zeros((filas,columnas))
for i in range(filas):
    for j in range(columnas):
        elem = random.randint(0,10)
        m[i][j] = elem
print('La matriz generada es:\n',m)

# Multiplicación
mr = m*escalar
print(f'La matriz resultante de la multiplicación con el escalar {escalar} es:\n',mr)