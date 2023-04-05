import random

print('Se pide crear un arreglo de número enteros y que este sea ordenado de forma descendente y de manera aleatoria.')
while True:
    arr = int(input('Ingrese el tamaño del arreglo (número entero): '))
    arreglo = list(range(arr))
    for n in range(0, len(arreglo)):
        arreglo[n]=int(input('Ingrese un número entero: '))

    for i in range(0, len(arreglo)):
        for j in range(0, i):
            if arreglo[i] > arreglo[j]:
                aux = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = aux

    print('El arreglo ordenado de manera descendente es:', arreglo)

    random.shuffle(arreglo)
    print('El arreglo ordenado de manera aleatoria con "shuffle" es:', arreglo)
    sample = random.sample(arreglo, len(arreglo))
    print('El arreglo ordenado de manera aleatoria con "sample" es:', sample)


    while True:
        seguir=input('¿Deseas seguir ordenando listas? (Si/No): ').lower()
        if seguir == 'no':
            quit()
        elif seguir != 'si':
            print('Ingrese una respuesta correcta.')
        else:
            break