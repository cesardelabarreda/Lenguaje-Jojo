
from Variable import Variable

class Atribute(Variable):
	def __init__(self, atrTipo = 0, atrEncap = 0):
		Variable.__init__(self, atrTipo)
		self.encap = atrEncap

	def __repr__(self):
		return "Tipo-%s Encap:-%s" %(str(self.tipo), str(self.encap))

	def __str__(self):
		return "Tipo-%s Encap:-%s" %(str(self.tipo), str(self.encap))
