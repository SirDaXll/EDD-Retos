# Clase pila
class pila:
    # Método para generar arreglo
    def __init__(self):
        self.stack = []

    # Método para apilar
    def push(self, item):
        self.stack.append(item)
    
    # Método para desapilar
    def pop(self):
        # Función para verificar si no está vacía la pila
        if not self.isEmpty():
            return self.stack.pop()
        # Pila vacía
        else:
            raise IndexError('La pila de libros está vacía')
        
    # Método para indicar el estado de la pila
    def __str__(self):
        return str(self.stack)
    
    # Método para indicar si la pila está vacía
    def isEmpty(self):
        return len(self.stack) == 0
    
    # Método para indicar el largo de la pila
    def size(self):
        return len(self.stack)
    
    # Método para indicar el elemento en el tope
    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    # Método para imprimir la pila
    def print(self):
        print('Listado de documentos actual en la pila:')
        for stack in reversed(self.stack):
            print(stack)


# Crear una instancia de la pila
pilaDocumentos = pila()

# Agregar los documentos iniciales
documentos = ['Informe Final', 'Guia de Estudio', 'Tesis 4', 'Seminario Osorno']
for documento in documentos:
    pilaDocumentos.push(documento)

# Imprimir el listado de documentos actual en la pila
pilaDocumentos.print()

# Agregar los documentos 'Avance Tesis' y 'Proyecto Integrador'
pilaDocumentos.push('Avance Tesis')
pilaDocumentos.push('Proyecto Integrador')

# Obtener el último elemento superior de la pila
ultimoElemento = pilaDocumentos.top()
print('Último elemento superior de la pila:', ultimoElemento)

# Eliminar el documento de la parte superior
documentoEliminado = pilaDocumentos.pop()
print('Documento eliminado de la parte superior:', documentoEliminado)

# Imprimir la pila de documentos actualizada
pilaDocumentos.print()

# Verificar si la pila de documentos está vacía
if pilaDocumentos.isEmpty() == 0:
    print('La pila de documentos está vacía.')
else:
    print('La pila de documentos no está vacía.')