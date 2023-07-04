# Clases necesarias.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class bidireccional:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    # A. Método para agregar.
    def add_final(self, dato):
        nuevonodo = Nodo(dato)
        if self.empty():
            self.primero = nuevonodo
            self.ultimo = nuevonodo
        else:
            nuevonodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevonodo
            self.ultimo = nuevonodo

    # A. Otro método para agregar.
    def add_inicio(self, dato):
        nuevoNodo = Nodo(dato)
        if self.empty():
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            nuevoNodo.siguiente = self.primero
            self.primero.anterior = nuevoNodo
            self.primero = nuevoNodo

    # E. Mostrar artículos (FALTA QUE LO HAGA ASCENDENTEMENTE).
    def print(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    # C. Buscar un artículo.
    def search(self, busqueda):
        actual = self.primero
        while actual:
            if actual.dato == busqueda:
                return True
            actual = actual.siguiente
        return False
    
    # B. Eliminar artículo (FALTA INDICAR QUE SEA POR EL CÓDIGO).
    def pop(self, busqueda):
        actual = self.primero
        while actual:
            if actual.dato == busqueda:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                break
            actual = actual.siguiente

    def empty(self):
        return self.primero is None
    
    # D. Método para actualizar la cantidad disponible.
    #def update(self, cantidad):
    #    ...

# Crear objeto.
inventario = bidireccional()

# A. Agregar artículos (FALTA IMPLEMENTAR DICCIONARIO: CÓDIGO; NOMBRE; DESCRIPCIÓN; CANTIDAD).
inventario.add_final('1, Mouse, Periférico, 10')
inventario.add_final('2, Teclado, Periférico, 20')

# B. Eliminar artículo (FALTA INDICAR SÓLO EL CÓDIGO).
inventario.pop('1, Mouse, Periférico, 10')

# C. Buscar artículo (FALTA BUSCAR SÓLO POR EL CÓDIGO).
inventario.search('2, Teclado, Periférico, 20')

# D. FALTA MÉTODO PARA ACTUALIZAR.
#inventario.update('2', '5')

# E. Mostrar artículos (FALTA QUE SEA ASCENDENTEMENTE POR EL CÓDIGO).
inventario.print()

# LOS MÉTODOS SIRVEN, PERO FALTA MENSAJE DE CONFIRMACIÓN.