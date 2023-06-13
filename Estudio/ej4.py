# Clase para la cola de productos del supermercado
class cola:
    # Método para generar arreglo
    def __init__(self):
        self.items = []

    # Método para agregar
    def agregar(self, x):
        self.items.append(x)

    # Método para eliminar
    def eliminar(self):
        # Función para verificar si está vacía la cola
        if self.estaVacia():
            raise ValueError('La cola está vacía.')
        # Eliminar de la cola
        return self.items.pop(0)
    
    # Método para indicar que la cola está vacía
    def estaVacia(self):
        return len(self.items) == 0
    
    # Método para indicar el estado de la cola
    def __str__(self):
        return str(self.items)

    # Método para imprimir la cola
    def print(self):
        print("Productos en la cola:")
        for items in self.items:
            print(items)

    # Método para invertir orden
    def invertir(self):
        self.items = self.items[::-1]

    # Método para vacia cola
    def vaciar(self):
        self.items = []

# Crear una instancia de la cola de supermercado
colaSupermercado = cola()

# Agregar productos a la cola
colaSupermercado.agregar('Atun')
colaSupermercado.agregar('Pan pita')
colaSupermercado.agregar('Queso sin lactosa')
colaSupermercado.agregar('Jamon')
colaSupermercado.agregar('Bebida energetica')
colaSupermercado.agregar('Jugo')

# Mostrar los productos en la cola
colaSupermercado.print()

# Eliminar el primer producto de la cola
productoEliminado = colaSupermercado.eliminar()
print('Producto eliminado:', productoEliminado)

# Mostrar los productos en la cola actualizada
colaSupermercado.print()

# Invertir el orden de los productos en la cola
colaSupermercado.invertir()

# Mostrar los productos en la cola con el orden invertido
colaSupermercado.print()

# Vaciar la cola de productos
colaSupermercado.vaciar()

# Mostrar los productos en la cola después de vaciarla
colaSupermercado.print()