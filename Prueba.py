class pila:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.previo = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

#Insert head and tail

    def insertar_cabeza(self,data):
        nuevo_nodo = pila(data)
        #En caso de que la lista este vacio se hace uso del condicional 
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = pila(data)
            self.cabeza.previo = nuevo_nodo
            self.cabeza = nuevo_nodo
        
#Insert tail

    def insertar_cola(self,data):
        nuevo_nodo = pila(data)
        #En caso de que la lista este vacio se hace uso del condicional 
        if self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.previo = pila(data)
            self.cabeza.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

#Remove an element
    def remove (self,data):
        actual = self.cabeza
        while actual:
            if actual.data == data:
                if actual.previo:
                    actual.previo.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.previo = actual.previo
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                if actual == self.cola:
                    self.cola = actual.previo
                return
            actual = actual.siguiente
#Remove all repeated elements

    def remove_repeated_elements(self):
         actual = self.cabeza
         lista_sin_repetidos = set()
         while actual:
             if actual.data in lista_sin_repetidos:
                  siguiente_nodo = actual.siguiente    
                  self.remove(actual.data)
                  actual = actual.siguiente
             else:
                 lista_sin_repetidos.add(actual.data)
                 actual = actual.siguiente
#Search for an element, returning it's index if found


#Size of the list
    def size(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador = contador + 1
            actual = actual.siguiente
        return contador
        
    def impresion(self):
        actual = self.cabeza
        while actual:
            print(actual.data, end=" <--> ")
            actual = actual.siguiente
        print("None")

prueba = ListaDoble()
prueba.insertar_cola(20)
prueba.insertar_cabeza(5)
prueba.insertar_cola(20)


print("Lista después de inserciones:")
prueba.impresion()

print("Tamaño de la lista:", prueba.size())

#print("Índice de 20:",prueba.search(20))

prueba.remove(5)
print("Lista después de eliminar 5:")
prueba.impresion()

prueba.remove_repeated_elements()
print("Lista después de eliminar duplicados:")
prueba.impresion()

print("Tamaño final de la lista:", prueba.size())
