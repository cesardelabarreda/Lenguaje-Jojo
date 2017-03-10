# encap:
# 0 - public
# 1 - private

class Function:
	

	def __init__(self, Encap = None):
		if Encap == None:
			self.encap = 0
		else:
			self.encap = Encap
		self.vars = {}
		self.params = []

	def emptyVars(self):
		return self.vars == {}

	def sizeVars(self):
		return len(self.vars)

	def emptyparams(self):
		return self.params == []

	def sizeparams(self):
		return len(self.params) 

	def existsVar(self, varId):
		return varId in self.vars

	def insertVar(self, varId, varType):
		if self.existsVar(varId):
			return 0

		self.vars[varId] = varType
		return 1

	def insertParam(self, paramType):
		self.params.append(paramType)
		return 1