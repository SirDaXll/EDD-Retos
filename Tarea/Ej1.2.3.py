print('Se solicita calcular el área y el perímetro de un triángulo según los valores que se introduzcan.')
while True:
    l1=float(input("Introduzca el valor del primer lado: "))
    l2=float(input("Introduzca el valor del segundo lado: "))
    l3=float(input("Introduzca el valor del tercer lado: "))

    peri=l1+l2+l3
    semiperi=peri/2
    area=(semiperi*(semiperi-l1)*(semiperi-l2)*(semiperi-l3))**0.5
    print("El perímetro del triángulo es:",peri)
    print("El área del triángulo es:",area)
    while True:
        i=input('¿Desea seguir? (Si/No): ').lower()
        if i == 'no':
            quit()
        elif i != 'si':
            print('Ingrese una respuesta correcta.')
        else:
            break