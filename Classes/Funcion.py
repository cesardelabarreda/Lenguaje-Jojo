from CuboSemantico import TypeConvertion
from Variable import Variable

"""
	Clase Funcion:
	Es un objeto que tiene varios atributos. 
	Tiene un diccionario de variables, donde la llave es el nombre de la variable 
		y dentro contiene un objeto Variable. 
	Tiene una lista de parametros, la cual cada posicion tiene una pareja de valores 
		donde la primera es una direccion de memoria del parametro y la segunda es el 
		tipo de parametro. 
	Tiene un atributo para el tipo de retorno. Tiene un atributo para la direccion 
		de memoria asociada. Tiene un atributo para el cuadruplo donde inicia.
	Tiene una memoria de la funcion, que sirve para asociar la funcion cuando se
		hace el era.
	Tiene el quadruplo inicial, para poder hacer el gosub especifico al quadruplo.
"""



class Function:
	def __init__(self, funcRetType):
		self.convert = TypeConvertion()
		self.vars = {}
		self.params = []
		self.retType = funcRetType
		self.memId = -1
		self.quadInicial = -1

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

		self.params.append([-1, paramType])
		return 1

	def actualizaParam(self, memId):
		self.params[self.sizeParams() - 1][0] = memId


	def getVariableType(self, varId):
		if self.existsVar(varId) == 0:
			return -1
		return self.vars[varId].tipo

	def getReturnType(self):
		return self.retType

	def getParams(self):
		return self.params

	def setMemVar(self, varId, mem):
		if self.existsVar(varId) == 0:
			return 0
		return self.vars[varId].setMemory(mem)

	def setMemFunc(self, iMem):
		self.memId = iMem
		return 1

	def setVarSize(self, varId, iSize):
		if self.existsVar(varId) == 0:
			return 0
		return self.vars[varId].setSize(iSize)

	def setVarOffset(self, varId, iOffset):
		if self.existsVar(varId) == 0:
			return 0
		return self.vars[varId].setOffset(iOffset)

	def getVarOffset(self, varId):
		if self.existsVar(varId) == 0:
			return 0
		return self.vars[varId].getOffset()

	def getVarSize(self, varId):
		if self.existsVar(varId) == 0:
			return -1
		return self.vars[varId].getSize()

	def setQuadInicial(self, iQuad):
		self.quadInicial = iQuad
		return 1

	def getQuadInicial(self):
		return self.quadInicial

	def getMemVar(self, varId):
		if self.existsVar(varId) == 0:
			return 0
		return self.vars[varId].getMemory()

	def getMemFunc(self):
		return self.memId

	def deleteVar(self, varId):
		if self.existsVar(varId) == 0:
			return 0
		del self.vars[varId]
		return 1

	def buscaVar(self, iMem):
		for sVar, value in self.vars.items():
			if self.vars[sVar].equalsMem(iMem):
				return sVar 
		return "_"

	def pprint(self, sFunc):
		print(" --- " + sFunc + " --- ")
		print(str(self))
		print(" ----------------- ")
	
	def __repr__(self):
		return "Vars: %s\nParams: %s\nretType: %s" %(str(self.vars), str(self.params), str(self.convert.convertType(self.retType)))

	def __str__(self):
		return "Vars: %s\nParams: %s\nretType: %s" %(str(self.vars), str(self.params), str(self.convert.convertType(self.retType)))

	