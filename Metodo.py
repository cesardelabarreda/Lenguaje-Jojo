from Funcion import Function

class Method(Function):
	def __init__(self, methRetType = 0, metEncap = 0):
		Function.__init__(self, metRetType)
		self.encap = metEncap