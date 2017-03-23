
from Metodo import Method
from Atributo import Atribute

class Class:
	def __init__(self):
		self.methods = {}
		self.atributes = {}
		self.classes = []

	def emptyMethod(self):
		return self.metodos == {}

	def emptyAtributes(self):
		return self.atributes == {}

	def emptyClasses(self):
		return self.classes == []

	def sizeMethods(self):
		return len(self.methods)

	def sizeAtributes(self):
		return len(self.atributes)

	def sizeClasses(self):
		return len(self.classes)

	def clearMethodVars(self, methodId):
		if self.existsMethod(methodId):
			self.methods[methodId].clearVars()

	def clearMethodParams(self, methodId):
		if self.existsMethod(methodId):
			self.methods[methodId].clearParams()

	def clearMethod(self, methodId):
		if self.existsMethod(methodId):
			self.methods[methodId].clear()

	def clearMethods(self):
		self.methods.clear()

	def clearClasses(self):
		self.classes.clear()

	def clearAtributes(self):
		self.atributes.clear()

	def clearPrivateAtributes(self):
		for atr in self.atributes:
			if atr.atrEncap == 1:
				del self.atributes[atr]

	def clear(self):
		self.clearMethods()
		self.clearAtributes()
		self.clearClasses()

	def existsHamon(self, classHamon):
		return classHamon in self.classes

	def existsMethod(self, methodId):
		return methodId in self.methods

	def existsAtribute(self, atributeId):
		return atributeId in self.atributes

	def existsMethodVariable(self, methodId, varId):
		if self.existsMethod(methodId):
			return self.methods[methodId].existsVar(varId)
		return 0

	def existsVariable(self, methodId, varId):
		if self.existsMethodVariable(methodId, varId):
			return 1
		return self.existsAtribute(varId)

	def insertHamon(self, classHamon):
		if self.existsHamon(classHamon):
			return 0
		self.classes.append(classHamon)
		return 1

	def insertMethod(self, methodId, methodRetType, methodEncap):
		if self.existsMethod(methodId):
			return 0

		meth = Method(methodRetType, methodEncap)
		self.methods[methodId] = meth
		return 1

	def insertVar(self, methodId, varId, varType):
		if self.existsMethod(methodId) == 0:
			return 0
		return self.methods[methodId].insertVar(varId, varType)

	def insertParam(self, methodId, varId, paramType):
		if self.existsMethod(methodId) == 0:
			return 0
		return self.methods[methodId].insertParam(varId, paramType)

	def insertAtribute(self, atrId, atrType, atrEncap):
		if self.existsAtribute(atrId):
			return 0

		atr = Atribute(atrType, atrEncap)
		self.atributes[atrId] = atr
		return 1

	def getAtributeType(self, atributeId):
		if self.existsAtribute(atributeId) == 0:
			return -1
		return self.atributes[atributeId].tipo

	def getVarType(self, methodId, varId):
		if self.existsMethod(methodId) == 0:
			return -1
		return self.methods[methodId].getVariableType(varId)

	def getMethodType(self, methodId):
		if self.existsMethod(methodId) == 0:
			return -1
		return self.methods[methodId].atrType

	def __repr__(self):
		return "Atributes: %s\n\nMethods: %s\n\nClasses: %s\n\n\n\n" %(str(self.atributes), str(self.methods), str(self.classes))

	def __str__(self):
		return "Atributes: %s\n\nMethods: %s\n\nClasses: %s\n\n\n\n" %(str(self.atributes), str(self.methods), str(self.classes))
