from CuboSemantico import TypeConvertion
from Variable import Variable

class Function:
	def __init__(self, funcRetType):
		self.convert = TypeConvertion()
		self.vars = {}
		self.params = []
		self.retType = funcRetType

	def emptyVars(self):
		return self.vars == {}
	
	def emptyParams(self):
		return self.params == []

	def sizeVars(self):
		return len(self.vars)

	def sizeParams(self):
		return len(self.params)

	def clearVars(self):
		self.vars.clear()

	def clearParams(self):
		self.params.clear()

	def clear(self):
		self.clearVars()
		self.clearParams()

	def existsVar(self, varId):
		return varId in self.vars

	def insertVar(self, varId, varType):
		if self.existsVar(varId):
			return 0

		var = Variable(varType)
		self.vars[varId] = var
		return 1

	def insertParam(self, varId, paramType):
		if self.insertVar(varId, paramType) == 0:
			return 0

		self.params.append(paramType)
		return 1

	def getVariableType(self, varId):
		if self.existsVar(varId) == 0:
			return -1
		return self.vars[varId].tipo

	def getReturnType(self):
		return self.retType

	def getParams(self):
		return self.params

	def deleteVar(self, varId):
		if self.existsVar(varId) == 0:
			return 0
		del self.vars[varId]
		return 1

	def pprint(self, sFunc):
		print(" --- " + sFunc + " --- ")
		print(str(self))
		print(" ----------------- ")
	
	def __repr__(self):
		return "Vars: %s\nParams: %s\nretType: %s" %(str(self.vars), str(self.params), str(self.convert.convertType(self.retType)))

	def __str__(self):
		return "Vars: %s\nParams: %s\nretType: %s" %(str(self.vars), str(self.params), str(self.convert.convertType(self.retType)))

	