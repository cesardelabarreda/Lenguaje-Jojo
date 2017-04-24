from CuboSemantico import TypeConvertion

class Variable:
	def __init__(self, varTipo):
		self.convert = TypeConvertion()
		self.tipo = varTipo
		self.memory = -1

	def setMemory(self, mem):
		self.memory = mem
		return 1

	def getMemory(self):
		return self.memory

	def pprint(self):
		print(str(self))

	def __repr__(self):
		return "Tipo-%s" %(str(self.convert.convertType(self.tipo)))

	def __str__(self):
		return "Tipo-%s" %(str(self.convert.convertType(self.tipo)))