
class Variable:
	def __init__(self, varTipo = 0):
		self.tipo = varTipo

	def __str__(self):
		return "%s" %(str(self.varTipo))