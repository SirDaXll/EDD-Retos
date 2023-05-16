import random, numpy

#def suma(matriz1, matriz2):
#    matrizResultado1 = 
#    return matrizResultado1

def mule(matrizResultado1, escalar):
    matrizResultado2 = matrizResultado1 * escalar
    return matrizResultado2

def mul(matrizResultado2, matriz3):
    matrizResultado3 = numpy.matmul(matrizResultado2, matriz3)
    return matrizResultado3


print('\nSe pide ingresar la cantidad de filas y de columnas para crear dos matrices con número aleatorios (entre 1 y 5) e imprimir la suma de estos.')

f1 = int(input('\nIngrese la cantidad de filas de la matriz 1: '))
c1 = int(input('Ingrese la cantidad de columnas de la matriz 1: '))
m1 = []
for i in range(f1):
    mf1 = []
    for j in range(c1):
        elem = random.randint(1,5)
        mf1.append(elem)
    m1.append(mf1)
print('La matriz 1 generada es:\n',m1)

f2 = int(input('\nIngrese la cantidad de filas de la matriz 2: '))
c2 = int(input('Ingrese la cantidad de columnas de la matriz 2: '))
m2 = []
for i in range(f2):
    mf2 = []
    for j in range(c2):
        elem = random.randint(1,5)
        mf2.append(elem)
    m2.append(mf2)
print('La matriz 2 generada es:\n',m2)

if f1==f2 and c1==c2:
    mr1 = suma(m1, m2)
    print('La matriz resultante de la suma es:\n',mr1)


print('\nLa matriz resultante de la suma anterior se debe multiplicar por un escalar entero que se debe ingresar (entre 1 y 10) e imprimir el resultado.')

e = int(input('Ingrese un escalar entero que se encuentre entre el 1 y el 10: '))
if e>=1 and e<=10:
    mr2 = mule(mr1, e)
    print(f'La matriz resultante de la multiplicación a un escalar {e} es:\n',mr2)


print('\nEl resultado de la matriz multiplicada se debe multiplicar nuevamente con otra matriz, la cuál se pedirá ingresar cada uno de sus valores, e imprimir el resultado final.')

f3 = int(input('\nIngrese la cantidad de filas de la matriz 2: '))
c3 = int(input('Ingrese la cantidad de columnas de la matriz 2: '))
m3 = []
for i in range(f3):
    mf3 = []
    for j in range(c3):
        elem = int(input(f'Ingrese el elemento [{i}][{j}]: '))
        mf3.append(elem)
    m3.append(mf2)
print('La matriz 3 generada es:\n',m3)

if f1==c3 or c1==f3:
    mr3 = mul(mr2, m3)
    print('El resultado de la multiplicación de ambas matrices es:\n', mr3)