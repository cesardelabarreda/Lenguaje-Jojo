"""
Clase atributo:

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
