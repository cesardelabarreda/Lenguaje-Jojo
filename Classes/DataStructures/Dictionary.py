# Dictionary.py
# Implementacion de la clase Dictionary, la cual utiliza un objeto que permite hashing.
# Para esta implementacion de diccionario, no se permiten los repetidos, lo que lo hace
#       un tanto parecido al map de C++.
# La documentacion para entender el funcionamiento de las listas fue obtenida del 
#       siguiente sitio: https://docs.python.org/2/tutorial/datastructures.html
# 16/ Enero/ 2017


class Dictionary:
	# Constructor de la clase Dictionary. Crea el objeto
	# Params: No tiene parametros de entrada
	# Ret: No tiene return
	def __init__(self):
		self.list = {}

	# Funcion que muestra si el Dictionary esta vacia o no. 
	# Trabaja en orden O(1)
	# Params: No tiene parametros de entrada
	# Ret: Un valor booleano, si esta vacia o no
	def empty(self):
		return self.list == {}

	# Funcion que muestra el tamano del Dictionary.
	# Trabaja en orden O(1)
	# Params: No tiene parametros de entrada
	# Ret: Un valor entero, el tamano
	def size(self):
		return len(self.list)


	# Funcion que inserta un valor a una llave dada.
	# Params: key - La llave
	# Params: value - El valor que se le va a agregar al Dictionary 
	# Ret: No tiene return
	def insert(self, key, value):
		self.list[key] = value

	# Funcion que obtiene el valor guardado dada una llave. Si no
	#       hay ningun valor asociado a esa llave, se marca un error.
	# Trabaja en orden O(1)
	# Params: key - La llave
	# Ret: El valor asociado con la llave.
	def at(self, key):
		return self.list.get(key)

	# Funcion que elimina el valor asociado a la llave, junto con la llave.
	# Trabaja en orden O(1)
	# Params: key - La llave
	# Ret: No tiene return
	def erase(self, key):
		del self.list[key]

	# Funcion que identifica si una llave ya fue asignada.
	# Trabaja en orden O(1)
	# Params: key - La llave
	# Ret: Un True o False, dependiendo si existe o no
	def find(self, key):
		return key in self.list

	# Funcion limpia el Dictionary. Borra todo su contenido.
	# Params: No tiene parametros de entrada
	# Ret: No tiene return
	def clear(self):
		self.list.clear()