# Realizar un algoritmo que permita simular el proceso de atención en un banco. Se debe crear 
# una lista con los nombres de los clientes. Utilizar clases y funciones.

# Clase para la cola de clientes del banco
class colaBanco:
    # Método para generar arreglo
    def __init__(self):
        self.items = []

    # Método para encolar cliente
    def encolar(self, x):
        self.items.append(x)

    # Método para desencolar cliente
    def desencolar(self):
        # Función para verificar si está vacía la cola de clientes
        if self.esta_vacia():
            raise ValueError('La cola de clientes está vacía.')
        # Desencolar cliente de la cola
        return self.items.pop(0)
    
    # Método para indicar que la cola está vacía
    def esta_vacia(self):
        return len(self.items) == 0
    
    # Método para indicar el estado de la cola
    def __str__(self):
        return str(self.items)
    
# Lista de clientes dentro del banco
clientes = ['Cliente 1', 'Cliente 2', 'Cliente 3', 'Cliente 4', 'Cliente 5']

# Creación objeto (cola)
atencionBanco = colaBanco()

# Se colan los clientes (del primero al último) (cliente = itinerador)
for cliente in clientes:
    atencionBanco.encolar(cliente)
    print('Ingresando a la cola:', cliente)

# Se imprime la cola
print('\nLo que hay en la cola:',atencionBanco,'\n')

# Se desencolan clientes de la cola (del primero al último)
while not atencionBanco.esta_vacia():
    cliente = atencionBanco.desencolar()
    print('Atendiendo cliente:', cliente)

# Se imprime la cola
print('\nLo que hay en la cola:',atencionBanco,'\n')