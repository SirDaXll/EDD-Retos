print('Se pide insertar elementos en un diccionario y obtener una ponderación.')

def notaFinal(lab1, lab2):
    pond1 = (lab1*30)/100
    pond2 = (lab2*70)/100
    return pond1 + pond2

estudiante = {}

for i in range(3):
    nombre = input(f'Ingresa el nombre del estudiante {i+1}: ')
    asignatura = input(f'Ingresa la asignatura del estudiante {i+1}: ')
    lab1 = float(input(f'Ingresa la primera nota del estudiante {i+1}: '))
    lab2 = float(input(f'Ingresa la segunda nota del estudiante {i+1}: '))
    promedio = round(notaFinal(lab1, lab2), 1)

    estudiante[f'Estudiante {i+1}'] = dict(
        nombre = nombre,
        asignatura = asignatura,
        lab1 = lab1,
        lab2 = lab2,
        promedio = promedio
    )

print(estudiante)