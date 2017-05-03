"""
Clase atributo:
	Hereda de la Clase Variable y ademas tiene implementado el atributo encap, el cual tiene el valor que representa si
		es publico o privado (0 o 1, respectivamente).
"""
from Variable import Variable

class Atribute(Variable):
	def __init__(self, atrTipo, atrEncap):
		Variable.__init__(self, atrTipo)
		self.encap = atrEncap

	def __repr__(self):
		return "Tipo-%s Encap-%s" %(str(self.convert.convertType(self.tipo)), str(self.convert.convertAccess(self.encap)))

	def __str__(self):
		return "Tipo-%s Encap-%s" %(str(self.convert.convertType(self.tipo)), str(self.convert.convertAccess(self.encap)))
