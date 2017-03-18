
class Variable:
	def __init__(self, varTipo = 0):
		self.tipo = varTipo

	def __repr__(self):
		return "Tipo-%s" %(str(self.tipo))

	def __str__(self):
		return "Tipo-%s" %(str(self.tipo))