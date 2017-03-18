from Funcion import Function

class Method(Function):
	def __init__(self, metRetType = 0, metEncap = 0):
		Function.__init__(self, metRetType)
		self.encap = metEncap

	def __repr__(self):
		return "Vars: %s\nParams: %s\nretType: %s\nEncap: %s\n\n" %(str(self.vars), str(self.params), str(self.retType), str(self.encap))

	def __str__(self):
		return "Vars: %s\nParams: %s\nretType: %s\nEncap: %s\n\n" %(str(self.vars), str(self.params), str(self.retType), str(self.encap))
