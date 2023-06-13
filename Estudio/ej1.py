print('Se pide registrar y buscar a pacientes.')

# Se crea una lista de pacientes
pacientes = []

# Agregar información de los pacientes (de 4) mediante teclado a un diccionario
for i in range(4):
    paciente = {}
    print('Ingrese la información del paciente', i + 1)
    paciente['Nombre'] = input('Nombre: ')
    paciente['Edad'] = int(input('Edad: '))
    paciente['Peso'] = float(input('Peso: '))
    # Lista para agregar múltiples síntomas
    sintomas = []
    while True:
        sintoma = input('Ingrese un síntoma (ingrese "fin" para terminar): ')
        if sintoma.lower() == 'fin':
            break
        sintomas.append(sintoma)
    paciente['Sintomas'] = sintomas
    pacientes.append(paciente)
    print()

while True:
    # Buscar un paciente específico por nombre
    nombreBuscar = input('Ingrese el nombre del paciente que desea buscar: ')
    pacienteEncontrado = None

    # Recorrer diccionarios en lista buscando un nombre coincidente
    for paciente in pacientes:
        if paciente['Nombre'] == nombreBuscar:
            pacienteEncontrado = paciente
            break

    # Mostrar la ficha personal del paciente encontrado
    if pacienteEncontrado:
        print('Ficha personal del paciente:')
        print('Nombre:', pacienteEncontrado['Nombre'])
        print('Edad:', pacienteEncontrado['Edad'])
        print('Peso:', pacienteEncontrado['Peso'])
        print('Síntomas:', pacienteEncontrado['Sintomas'])
    
    # Error
    else:
        print(f'No se encontró ningún paciente con el nombre {nombreBuscar}.')
    
    # ¿Seguir?
    seguir = input('¿Deseas seguir? (Si/No): ').lower()
    if seguir == 'no':
        print('Saliendo...\n')
        quit()
    elif seguir != 'si':
        print('Ingrese una respuesta correcta.')
    else:
        pass