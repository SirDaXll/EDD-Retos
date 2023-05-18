print('Se pide determinar la distancia entre dos puntos (x1,y1, z1) y (x2, y2, z2).')
while True:
    x1=float(input('Ingrese el valor de x1: '))
    y1=float(input('Ingrese el valor de y1: '))
    z1=float(input('Ingrese el valor de z1: '))

    x2=float(input('Ingrese el valor de x2: '))
    y2=float(input('Ingrese el valor de y2: '))
    z2=float(input('Ingrese el valor de z2: '))

    dist=((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5
    print('La distancia entre ambos puntos es: ',dist)
    while True:
        aux=input('¿Deseas seguir calculando la distancia entre dos puntos? (Si/No): ').lower()
        if aux == 'no':
            quit()
        elif aux != 'si':
            print('Ingrese una respuesta correcta.')
        else:
            break