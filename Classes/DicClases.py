
from Clase import Class

class DicClass:
	def __init__(self):
		self.classes = {}

	def empty(self):
		return self.classes == {}

	def size(self):
		return len(self.classes)

	def clearClass(self, classId):
		if self.existsClass(classId):
			self.classes[classId].clear()

	def clear(self):
		self.classes.clear()

	def existsClass(self, classId):
		return classId in self.classes

	def existsMethod(self, classId, methodId):
		if self.existsClass(classId) == 0:
			return 0

		if self.classes[classId].existsMethod(methodId):
			return 1

		for clas in self.classes[classId].classes:
			bRet = self.existsMethod(clas, methodId)
			if bRet:
				return 1
		return 0

	def existsAtribute(self, classId, atributeId):
		if self.existsClass(classId) == 0:
			return 0

		if self.classes[classId].existsAtribute(atributeId):
			return 1
	 
		for clas in self.classes[classId].classes:
			if self.existsAtribute(clas, atributeId) == 1:
				return 1
		return 0

	def existsVariable(self, classId, methodId, varId):
		if self.existsClass(classId) == 0:
			return 0

		if self.classes[classId].existsVariable(methodId, varId):
			return 1
		return self.existsAtribute(classId, varId)

	def getAtributeSize(self, classId, methodId):
		if self.existsClass(classId) == 0:
			return 0

		if self.classes[classId].existsMethod(methodId):
			return 1
		return self.classes[classId].getAtributeSize() 

	def getAtributes(self, classId, methodId):
		if self.existsClass(classId) == 0:
			return 0

		if self.classes[classId].existsMethod(methodId):
			return 1
		return self.classes[classId].getAtributes() 

	def insertHamon(self, classId, classHamon):
		if self.existsClass(classId) == 0:
			return 0
		if self.existsClass(classHamon) == 0:
			return 0
		return self.classes[classId].insertHamon(classHamon)

	def insertClass(self, classId):
		if self.existsClass(classId):
			return 0

		clas = Class()
		self.classes[classId] = clas

	def insertMethod(self, classId, methodId, methodRetType, methodEncap):
		if self.existsClass(classId) == 0:
			return 0
		return self.classes[classId].insertMethod(methodId, methodRetType, methodEncap)

	def insertVar(self, classId, methodId, varId, varType):
		if self.existsClass(classId) == 0:
			return 0
		return self.classes[classId].insertVar(methodId, varId, varType)

	def insertParam(self, classId, methodId, varId, paramType):
		if self.existsClass(classId) == 0:
			return 0
		return self.classes[classId].insertParam(methodId, varId, paramType)

	def insertAtribute(self, classId, atrId, atrType, atrEncap):
		if self.existsClass(classId) == 0:
			return 0
		return self.classes[classId].insertAtribute(atrId, atrType, atrEncap)
	
	def getAtributeType(self, classId, atributeId):
		if self.existsClass(classId) == 0:
			return -1

		iRet = self.classes[classId].getAtributeType(atributeId)
		if iRet != -1:
			return iRet
	 
		for clas in self.classes[classId].classes:
			iRet = self.getAtributeType(clas, atributeId)
			if iRet != -1:
				return iRet
		return -1


	def getVariableType(self, classId, methodId, varId):		
		if self.existsClass(classId) == 0:
			return -1

		iRet = self.classes[classId].getVarType(methodId, varId)
		if iRet != -1:
			return iRet

		return self.getAtributeType(classId, varId)

	def getMethodReturnType(self, classId, methodId):
		if self.existsClass(classId) == 0:
			return -1

		iRet = self.classes[classId].getMethodReturnType(methodId)
		if iRet != -1:
			return iRet

		for clas in self.classes[classId].classes:
			iRet = self.getMethodReturnType(clas, methodId)
			if iRet != -1:
				return iRet
		return -1

	def getMethodEncap(self, classId, methodId):
		if self.existsClass(classId) == 0:
			return -1

		iRet = self.classes[classId].getMethodEncap(methodId)
		if iRet != -1:
			return iRet

		for clas in self.classes[classId].classes:
			iRet = self.getMethodEncap(clas, methodId)
			if iRet != -1:
				return iRet
		return -1

	def getParams(self, classId, methodId):
		if self.existsClass(classId) == 0:
			return -1

		iRet = self.classes[classId].getParams(methodId)
		if iRet != -1:
			return iRet

		for clas in self.classes[classId].classes:
			iRet = self.getParams(clas, methodId)
			if iRet != -1:
				return iRet
		return -1

	def setVarSizeOff(self, classId, methodId, varId, iSize, iOffset):
		if self.existsClass(classId) == 0:
			return 0

		iRet = self.classes[classId].setVarSize(methodId, varId, iSize)
		if iRet != 0:
			return self.classes[classId].setVarOffset(methodId, varId, iOffset)

		for clas in self.classes[classId].classes:
			iRet = self.setVarSizeOff(self, clas, methodId, varId, iSize, iOffset)
			if iRet != 0:
				return iRet
		return 0

	def setVarSize(self, classId, methodId, varId, iSize):
		if self.existsClass(classId) == 0:
			return 0

		iRet = self.classes[classId].setVarSize(methodId, varId, iSize)
		if iRet != 0:
			return self.classes[classId].setVarSize(methodId, varId, iSize)

	def setVarOffset(self, classId, methodId, varId, iOffset):
		if self.existsClass(classId) == 0:
			return 0

		iRet = self.classes[classId].setVarOffset(methodId, varId, iOffset)
		if iRet != 0:
			return self.classes[classId].setVarOffset(methodId, varId, iOffset)

	def getVarOffset(self, classId, methodId, varId):
		if self.existsClass(classId) == 0:
			return 0
		return self.classes[classId].getVarOffset(methodId, varId)

	def getVarSize(self, classId, methodId, varId):
		if self.existsClass(classId) == 0:
			return -1
		return self.classes[classId].getVarSize(methodId, varId)


	def setMemVar(self, classId, methodId, varId, mem):
		if self.existsClass(classId) == 0:
			return 0
		return self.classes[classId].setMemVar(methodId, varId, mem)

	def setMemFunc(self, classId, methodId, mem):
		if self.existsClass(classId) == 0:
			return 0
		return self.classes[classId].setMemFunc(methodId, mem)


	def getMemVar(self, classId, methodId, varId):
		if self.existsClass(classId) == 0:
			return 0
		return self.classes[classId].getMemVar(methodId, varId)
		
	def getMemFunc(self, classId, methodId):
		if self.existsClass(classId) == 0:
			return -1
		return self.classes[classId].getMemFunc(methodId)

	def pprint(self):
		iTam = self.size()
		for clas in self.classes:
			self.classes[clas].pprint(clas)
			iTam = iTam - 1
			if iTam > 0:
				print("\n")

	def __repr__(self):
		return "%s" %(str(self.classes))

	def __str__(self):
		return "%s" %(str(self.classes))