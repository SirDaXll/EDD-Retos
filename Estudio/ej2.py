# Función para eliminar elementos repetidos en una lista
def eliminarRepetidos(lista):
    listaSinRepetidos = []
    for elemento in lista:
        if elemento not in listaSinRepetidos:
            listaSinRepetidos.append(elemento)
    return listaSinRepetidos

# Aquí empieza
print('Se pide realizar diferentes modificaciones a una tupla.')

frutas = ['manzana', 'platano', 'pera', 'naranja', 'frutilla', 'manzana']
print('La tupla es:\n',frutas)

# Llamar función para eliminar elementos repetidos
frutas = eliminarRepetidos(frutas)
print('La tupla actual es:\n',frutas)

# Convertir la lista de frutas en un conjunto para eliminar elementos repetidos
#frutas = list(set(frutas))

# Agregar la fruta 'mango' por teclado
frutaNueva = input('Ingrese una fruta para agregar: ')
frutas.append(frutaNueva)
print('La tupla actual es:\n',frutas)

# Eliminar la fruta 'platano' si existe
if 'platano' in frutas:
    frutas.remove('platano')
print('La tupla actual es:\n',frutas)

# Calcular la cantidad de frutas que existen
cantidadFrutas = len(frutas)

print('Lista de frutas:', frutas)
print('Cantidad de frutas:', cantidadFrutas)