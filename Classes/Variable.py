from CuboSemantico import TypeConvertion

class Variable:
	def __init__(self, varTipo):
		self.convert = TypeConvertion()
		self.tipo = varTipo
		self.memory = -1
		self.size = 0
		self.offset = 1

	def setMemory(self, iMem):
		self.memory = iMem
		return 1

	def setSize(self, iSize):
		self.size = iSize

	def setOffset(self, iOffset):
		self.offset = iOffset

	def getMemory(self):
		return self.memory

	def getSize(self):
		return self.size

	def getOffset(self):
		return self.offset

	def equalsMem(self, iMem):
		return self.memory == iMem

	def pprint(self):
		print(str(self))

	def __repr__(self):
		return "Tipo-%s" %(str(self.convert.convertType(self.tipo)))

	def __str__(self):
		return "Tipo-%s" %(str(self.convert.convertType(self.tipo)))