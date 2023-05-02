# Suma de Matrices traspuestas
import numpy
import random

def suma(m1, m2):
    m_final_suma = numpy.add(m1, m2)
    return m_final_suma
def transpuesta(mt):
    matrizt = numpy.transpose(mt)
    return matrizt

# Ingreso de Matriz 1
f1 = int(input('\nMatriz 1:\nIngrese la cantidad de filas de la matriz 1: '))
c1 = int(input('Ingrese la cantidad de columnas de la matriz 1: '))

# Ingreso de Matriz 2
f2 = int(input('\nMatriz 2:\nIngrese la cantidad de filas de la matriz: '))
c2 = int(input('Ingrese la cantidad de columnas de la matriz: '))

if (f1==f2 and c2==f2):
    print('Ingresando los elementos de la matriz 1...')
    # Crear matriz con solo ceros
    m1 = numpy.zeros((f1,c1))
    for i in range(f1):
        for j in range(c1):
            elem = random.randint(0,10)
            #elem = int(input(f'Ingrese el elemento [{i}][{j}]: '))
            m1[i][j] = elem

    print('Ingresando los elementos de la matriz 2...')
    # Crear matriz con solo ceros
    m2 = numpy.zeros((f2,c2))
    for i in range(f2):
        for j in range(c2):
            elem = random.randint(0,10)
            #elem = int(input(f'Ingrese el elemento [{i}][{j}]: '))
            m2[i][j] = elem

    print('\nLa matriz 1 es:\n',m1)
    print('\nLa matriz 2 es:\n',m2)

    # Transpuesta Matrices
    mt1 = transpuesta(m1)
    mt2 = transpuesta(m2)
    print('\nLa matriz 1 transpuesta es:\n',mt1)
    print('\nLa matriz 2 transpuesta es:\n',mt2)

    # Suma Matrices
    m_final_suma = suma(mt1, mt2)
    print('\nLa matriz resultado de la suma es:')
    print(m_final_suma)

else:
    print('La suma de matrices no se puede realizar debido a que se incumple la definición de ésta.')
