import numpy
import random

# Ingreso de Matriz
f = int(3)
c = int(3)

m = numpy.zeros((f,c))
for i in range(f):
    for j in range(c):
        elem = random.randint(5, 10)
        m[i][j] = elem
print('\nLa matriz de 3 x 3 es:\n',m)

determinante = numpy.linalg.det(m)
print('\nEl determinante de la matriz es:\n', determinante)