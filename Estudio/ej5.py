print('Se pide registrar una tabla como diccionario.')

# Se crea una lista para la tabla
tabla = []

# Agregar información de 3 capitales mediante teclado a un diccionario
for i in range(3):
    diccionario = {}
    print('Ingrese la información de la capital', i + 1)
    diccionario['Capital'] = input('Ingrese el nombre de la ciudad: ')
    diccionario['Región'] = input('Ingrese el nombre de la región: ')
    comunas = []
    for j in range(3):
        comuna = input('Ingrese el nombre de la comuna: ')
        comunas.append(comuna)
    diccionario['Comunas'] = comunas
    coordenadas = []
    latitud = float(input('Ingrese la latitud de la capital: '))
    longitud = float(input('Ingrese la longitud de la capital: '))
    coordenadas.append(latitud)
    coordenadas.append(longitud)
    diccionario['Coordenadas Capital'] = coordenadas
    tabla.append(diccionario)

print(tabla)
