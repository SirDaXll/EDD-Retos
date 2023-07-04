# A. Clases requeridas.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class circularBidireccional:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    # B. Método para agregar (FALTA IMPLEMENTAR DICCIONARIO: NOMBRE; TELEFONO; CORREO).
    def add_inicio(self, dato):
        nuevoNodo = Nodo(dato)
        if self.empty():
            nuevoNodo.siguiente = nuevoNodo
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            nuevoNodo.siguiente = self.primero
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo
            self.primero = nuevoNodo

    # B. Otro método para agregar (FALTA IMPLEMENTAR DICCIONARIO: NOMBRE; TELEFONO; CORREO).
    def add_final(self, dato):
        nuevoNodo = Nodo(dato)
        if self.empty():
            nuevoNodo.siguiente = nuevoNodo
            self.primero = nuevoNodo
        else:
            nuevoNodo.siguiente = self.primero
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo

    # C. Método para mostrar.
    def print(self):
        if self.empty():
            return print('La lista está vacía.')
        actual = self.primero
        while True:
            print(actual.dato)
            actual = actual.siguiente
            if actual == self.primero:
                break

    # D. Método para buscar (FALTA INDICAR QUE SEA POR NOMBRE).
    def search(self, busqueda):
        if self.empty():
            return False
        actual = self.primero
        while True:
            if actual.dato == busqueda:
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False

    # E. Método para eliminar (FALTA INDICAR QUE SEA POR NOMBRE).
    def pop(self, busqueda):
        actual = self.primero
        anterior = None
        while True:
            if actual.dato == busqueda:
                if anterior:
                    anterior.siguiente = actual.siguiente
                    if actual == self.primero:
                        self.primero = actual.siguiente
                else:
                    temp = actual
                    while temp.siguiente != self.primero:
                        temp = temp.siguiente
                    temp.siguiente = actual.siguiente
                    self.primero = actual.siguiente
                break
            anterior = actual
            actual = actual.siguiente
            if actual == self.primero:
                break

    # F. Método para verificar.
    def empty(self):
        return self.primero is None

# Crear objeto.
contactos = circularBidireccional()

# B. Agregar contacto (IMPLEMENTAR DICCIONARIO: NOMBRE; TELEFONO; CORREO).
contactos.add_final('Diego, 123456, diego@ulagos.cl')
contactos.add_final('Gabriel, 654321, gabriel@ulagos.cl')

# C. Mostrar contactos.
contactos.print()

# D. Buscar por nombre (FALTA EL DICCIONARIO).
contactos.search('Diego, 123456, diego@ulagos.cl')

# E. Eliminar contacto (FALTA EL DICCIONARIO).
contactos.pop('Diego, 123456, diego@ulagos.cl')

# F. Verificar si la lista está vacía.
contactos.empty()

# C. Mostrar contactos.
print('\n')
contactos.print()

# LOS MÉTODOS SIRVEN, PERO FALTA MENSAJE DE CONFIRMACIÓN.