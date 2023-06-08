# Realizar un algoritmo que permita simular el proceso de apilar libros en una biblioteca, y 
# luego ir sacándolos utilizando el principio de pilas. Utilizar clases y funciones.

# Clase para apilar libros
class pilaLibros:
    # Método para generar arreglo
    def __init__(self):
        self.stack = []

    # Método para apilar libros
    def push(self, item):
        self.stack.append(item)
    
    # Método para desapilar libros
    def pop(self):
        # Función para verificar si no está vacía la pila de libros
        if not self.is_empty():
            return self.stack.pop()
        # Pila de libros vacía
        else:
            raise IndexError("La pila de libros está vacía")
        
    # Método para entregar la pila
    def __str__(self):
        return str(self.stack)
    
    # Método para indicar si la pila está vacía
    def is_empty(self):
        return len(self.stack) == 0
    
    # Método para indicar el largo de la pila
    def size(self):
        return len(self.stack)

# Lista de libros en la biblioteca
libros = ["Libro 1", "Libro 2", "Libro 3", "Libro 4", "Libro 5"]

# Creación objeto (pila)
librosBiblioteca = pilaLibros()

# Se apilan algunos libros (de abajo hacía arriba)
for libro in libros:
    librosBiblioteca.push(libro)
    print("Colocando libro:", libro)

# Se imprime la pila
print('\nLo que hay en la pila:',librosBiblioteca,'\n')

# Sacamos los libros de la pila (de arriba hacía abajo)
while not librosBiblioteca.is_empty():
    libro = librosBiblioteca.pop()
    print("Sacando libro:", libro)

# Se imprime la pila
print('\nLo que hay en la pila:',librosBiblioteca,'\n')