
from Variable import Variable

class Atribute(Variable):
	def __init__(self, atrTipo = 0, atrEncap = 0):
		Variable.__init__(self, varTipo)
		self.encap = atrEncap

	def __str__(self):
		return "%s %s" %(str(self.tipo), str(self.scope))