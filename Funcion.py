from Variable import Variable

class Function:
	def __init__(self, funcRetType = 0):
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

	def deleteVar(self, varId):
		if self.existsVar(varId) == 0:
			return 0
		del self.vars[varId]
		return 1

	def existsVar(self, varId):
		return varId in self.vars

	def insertVar(self, varId, varType = 0):
		if self.existsVar(varId):
			return 0

		var = Variable(varType)
		self.vars[varId] = var
		return 1

	def insertParam(self, paramType):
		self.params.append(paramType)
		return 1

	