"""
	Clase Variable
	La clase variable tiene un atributo tipo para el tipo de dato.
	Tambien tiene un atributo memoria que almacena la direccion de memoria de 
		la variable, 
	Tambien tiene un atributo size que almacena un 0 si no es arreglo, o un
		entero positivo si almacena un arreglo.
	El atributo offset empezo siendo util cuando se planeaba tener arreglos de
		objetos, pero el resulto siendo inutil. No se borra por miedo a que termine
		siendo importante.
"""

from CuboSemantico import TypeConvertion

class Variable:
	def __init__(self, varTipo):
		self.convert = TypeConvertion()
		self.tipo = varTipo
		self.memory = -1
		self.size = 0
		self.offset = 1

	def setMemory(self, iMem):
		self.memory = iMem
		return 1

	def setSize(self, iSize):
		self.size = iSize
		return 1

	def setOffset(self, iOffset):
		self.offset = iOffset
		return 1
		
	def getMemory(self):
		return self.memory

	def getSize(self):
		return self.size

	def getOffset(self):
		return self.offset

	def equalsMem(self, iMem):
		return self.memory == iMem

	def pprint(self):
		print(str(self))

	def __repr__(self):
		return "Tipo-%s" %(str(self.convert.convertType(self.tipo)))

	def __str__(self):
		return "Tipo-%s" %(str(self.convert.convertType(self.tipo)))