class Queue:
    # Constructor de la clase Queue. Crea la lista
    # Params: No tiene parametros de entrada
    # Ret: No tiene return
    def __init__(self):
        self.list = []

    # Funcion que muestra si la Queue esta vacia o no. 
    # Trabaja en orden O(1)
    # Params: No tiene parametros de entrada
    # Ret: Un valor booleano, si esta vacia o no
    def empty(self):
        return self.list == []

    # Funcion que muestra el tamano de la Queue.
    # Trabaja en orden O(1)
    # Params: No tiene parametros de entrada
    # Ret: Un valor entero, el tamano de la lista
    def size(self):
        return len(self.list)
    
    # Funcion que saca al siguiente elemento de la Queue.
    # Trabaja en orden O(1)
    # Params: No tiene parametros de entrada
    # Ret: No tiene return
    def pop(self):
        return self.list.pop(0)

    # Funcion que agrega un elemento a la Queue.
    # Trabaja en orden O(1)
    # Params: value - El valor que se le va a agregar a la Queue
    # Ret: No tiene return
    def push(self, value):
        self.list.append(value)

    # Funcion que obtiene el siguiente elemento de la Queue.
    # Trabaja en orden O(1)
    # Params: value - El valor que se le va a agregar a la Queue
    # Ret: No tiene return
    def front(self):
        return self.list[0]

    # Funcion limpia la Queue. Borra todo su contenido.
    # Params: No tiene parametros de entrada
    # Ret: No tiene return
    def clear(self):
        self.list.clear()