while True:
    # Pedir al usuario una palabra
    palabra = input("Introduce una palabra para contar c/u de sus vocales: ").lower()

    # Inicializar contadores para cada vocal
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0

    # Recorrer la palabra y contar cada vocal
    for letra in palabra:
        if letra == 'a' or letra == 'A' or letra == 'á' or letra == 'Á':
            a_count += 1
        elif letra == 'e' or letra == 'E' or letra == 'é' or letra == 'É':
            e_count += 1
        elif letra == 'i' or letra == 'I' or letra == 'í' or letra == 'Í':
            i_count += 1
        elif letra == 'o' or letra == 'O' or letra == 'ó' or letra == 'Ó':
            o_count += 1
        elif letra == 'u' or letra == 'U' or letra == 'ú' or letra == 'Ú' or letra == 'ü':
            u_count += 1

    # Mostrar los resultados
    print("Número de veces que aparece la vocal 'a': ", a_count)
    print("Número de veces que aparece la vocal 'e': ", e_count)
    print("Número de veces que aparece la vocal 'i': ", i_count)
    print("Número de veces que aparece la vocal 'o': ", o_count)
    print("Número de veces que aparece la vocal 'u': ", u_count)
    while True:
        seguir = input('¿Deseas seguir contando vocales? (Si/No): ').lower()
        if seguir == 'no':
            print('Saliendo...\n')
            quit()
        elif seguir != 'si':
            print('Ingrese una respuesta correcta.')
        else:
            break