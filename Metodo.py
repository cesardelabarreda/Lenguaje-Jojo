from Funcion import Function

class Method(Function):
	def __init__(self, metRetType = 0, metEncap = 0):
		Function.__init__(self, metRetType)
		self.encap = metEncap