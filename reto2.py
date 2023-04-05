print('Se pide crear un algoritmo en el que se guarden los nombres y el RUT de 5 personas, y posteriormente se ordenen alfabéticamente y ascendentemente respectivamente.')
nombre=list(range(5))
rut=list(range(5))

while True:
    for n in range(0, 5):
        nombre[n]=str(input('Ingrese el nombre: '))
        rut[n]=int(input('Ingrese el RUT sin puntos ni dígito verificador: '))
        print('\n')

    for i in range(0, len(nombre)):
        for j in range(0, i):
            if nombre[i] < nombre[j]:
                aux = nombre[i]
                nombre[i] = nombre[j]
                nombre[j] = aux

    for i in range(0, len(rut)):
        for j in range(0, i):
            if rut[i] < rut[j]:
                aux = rut[i]
                rut[i] = rut[j]
                rut[j] = aux

    ##Facilmente puedo usar la función 'sorted()' pero meh

    print('Los nombres ordenados alfabeticamente es:', nombre)
    print('Los RUT ordenados de manera ascendente es:', rut)

    while True:
        seguir=input('¿Deseas seguir ordenando listas? (Si/No): ').lower()
        if seguir == 'no':
            quit()
        elif seguir != 'si':
            print('Ingrese una respuesta correcta.')
        else:
            break