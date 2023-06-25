class Nodo():
    dato = None
    siguiente = None
        
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def agregar_al_final(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    if nodo_inicial is None:
        return nuevo_nodo
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial

def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo

def imprimir_lista(nodo):
    while nodo is not None:
        print(nodo.dato)
        nodo = nodo.siguiente

def obtener_top(nodo_inicial):
    return nodo_inicial

def obtener_cola(nodo_inicial):
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    return temporal

def existe(nodo, busqueda):
    while nodo is not None:
        if nodo.dato == busqueda:
            return True
        nodo = nodo.siguiente
    return False

def eliminar(nodo, busqueda):
    if nodo is None:
        return None
    if nodo.dato == busqueda:
        return nodo.siguiente
    temporal = nodo
    while temporal.siguiente is not None:
        if temporal.siguiente.dato == busqueda:
            if temporal.siguiente.siguiente is not None:
                temporal.siguiente = temporal.siguiente.siguiente
            else:
                temporal.siguiente = None
            return nodo
        temporal = temporal.siguiente
    return nodo


nodo_inicial = None

while True:
    print('Algoritmos para modificar lista enlazada:')
    print('A) Agregar una fruta al final de la lista')
    print('B) Agregar una fruta al inicio de la lista')
    print('C) Eliminar una fruta')
    print('D) Imprimir la lista actual')
    print('E) Obtener cabecera')
    print('F) Obtener cola')
    print('X) Salir')

    opcion = input('Selecciona una opción (sólo la letra): ').upper()

    if opcion == 'A':
        fruta = input('Ingrese el nombre de la fruta: ')
        nodo_inicial = agregar_al_final(nodo_inicial, fruta)
        print('Fruta agregada al final de la lista.')

    elif opcion == 'B':
        fruta = input('Ingrese el nombre de la fruta: ')
        nodo_inicial = agregar_al_inicio(nodo_inicial, fruta)
        print('Fruta agregada al inicio de la lista.')

    elif opcion == 'C':
        fruta = input('Ingrese el nombre de la fruta a eliminar: ')
        nodo_inicial = eliminar(nodo_inicial, fruta)
        print('Fruta eliminada de la lista.')

    elif opcion == 'D':
        print('Lista actual:')
        imprimir_lista(nodo_inicial)

    elif opcion == 'E':
        cabecera = obtener_top(nodo_inicial)
        if cabecera is not None:
            print('Cabecera:', cabecera.dato)
        else:
            print('La lista está vacía.')

    elif opcion == 'F':
        cola = obtener_cola(nodo_inicial)
        if cola is not None:
            print('Cola:', cola.dato)
        else:
            print('La lista está vacía.')

    elif opcion == 'X':
        print('Saliendo...')
        break

    else:
        print('Opción inválida. Intenta nuevamente.')
