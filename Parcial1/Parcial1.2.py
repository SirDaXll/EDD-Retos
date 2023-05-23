import numpy
import random

def multiplicacion(m1, m2):
    mresultante = numpy.multiply(m1, m2)
    return mresultante

# Ingreso de Matriz 1
f1 = int(3)
c1 = int(3)

# Ingreso de Matriz 2
f2 = int(3)
c2 = int(3)

if (f1==c2 or c1==f2):
    m1 = numpy.zeros((f1,c1))
    for i in range(f1):
        for j in range(c1):
            elem = random.randint(-10, -5)
            m1[i][j] = elem

    m2 = numpy.zeros((f2,c2))
    for i in range(f2):
        for j in range(c2):
            elem = random.randint(-10, -5)
            m2[i][j] = elem

    print('\nLa matriz 1 es:\n',m1)
    print('\nLa matriz 2 es:\n',m2)

    # Multiplicación
    mresultante = multiplicacion(m1, m2)
    print('\nLa matriz resultado de la multiplicación es:')
    print(mresultante)

else:
    print('La multiplicación de matrices no se puede realizar debido a que no poseen las mismas dimensiones.')