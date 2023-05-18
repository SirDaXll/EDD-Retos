print('Se pide mostrar una calificación cualitativa para cada número real, el cuál representa la calificación numérica de un exámen.')
while True:
    cal=float(input('Ingresa la calificación (comprendido entre 1.0 y 7.0): '))
    if cal>=1 and cal<=7:
        if cal<4:
            print("Reprobado")
        elif cal>=4 or cal<5:
            print("Aprobado")
        elif cal>=5 or cal<6:
            print("Notable")
        elif cal>=6 or cal<=7:
            print("Sobresaliente")
        while True:
            i=input('¿Desea seguir? (Si/No): ').lower()
            if i == 'no':
                quit()
            elif i != 'si':
                print('Ingrese una respuesta correcta.')
            else:
                break
    else:
        print('Ingrese una calificación correcta.')