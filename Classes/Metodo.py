"""
Clase Metodo:
	Hereda de la Clase Funcion y ademas tiene implementado el atributo encap, el cual tiene el valor que representa si
		es publico o privado (0 o 1, respectivamente).
"""

from Funcion import Function

class Method(Function):
	def __init__(self, metRetType, metEncap):
		Function.__init__(self, metRetType)
		self.encap = metEncap

	def getEncap(self):
		return self.encap

	def __repr__(self):
		return "Vars: %s\nParams: %s\nretType: %s\nEncap: %s" %(str(self.vars), str(self.params), str(self.retType), str(self.encap))

	def __str__(self):
		return "Vars: %s\nParams: %s\nretType: %s\nEncap: %s" %(str(self.vars), str(self.params), str(self.retType), str(self.encap))
