import random

while True:
    # Generar tamaño aleatorio del arreglo entre 10 y 30
    tamano = random.randint(10, 30)

    # Generar el arreglo aleatorio
    arreglo = []
    for i in range(tamano):
        arreglo.append(random.randint(0, 100))

    while True:
        # Imprimir el arreglo generado
        print("Arreglo generado aleatoriamente:\n")
        print(arreglo)

        # Solicitar al usuario el elemento a buscar
        busqueda = int(input("\nIngrese el número que desea buscar en el arreglo: "))

        # Buscar el elemento en el arreglo
        encontrado = False
        for i in range(tamano):
            if arreglo[i] == busqueda:
                encontrado = True
                print(f"El número {busqueda} fue encontrado en la posición {i} del arreglo.\n")
                break

        if not encontrado:
            print(f"El número {busqueda} no fue encontrado en el arreglo.\n")

        while True:
            # Preguntando por el arreglo ya generado
            seguir = input('¿Deseas seguir encontrando números en el arreglo? (Si/No): ').lower()
            aux = True
            if seguir == 'no':
                aux = False
                break
            elif seguir != 'si':
                print('Ingrese una respuesta correcta.')
            else:
                break
        if aux == False:
            break
        else:
            pass

    while True:
        # Preguntando para generar otro arreglo
        seguir = input('¿Deseas generar otro arreglo de números? (Si/No): ').lower()
        if seguir == 'no':
            print('Saliendo...\n')
            quit()
        elif seguir != 'si':
            print('Ingrese una respuesta correcta.')
        else:
            break