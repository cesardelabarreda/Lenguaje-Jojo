import copy
from Util import Util
from CuboSemantico import TypeConvertion
from DataStructures.Dictionary import Dictionary
from DataStructures.Stack import Stack
from DataStructures.Queue import Queue

class MemoryTypes:
	def __init__(self, iBaseVars, iLimits):
		self.iBaseVar = iBaseVars
		self.iCantVar = {}
		self.iLimit = iLimits

		for i in range(0, 4):
			self.iCantVar[i] = 0

		self.mem = {}

	def exists(self, iMemId):
		return iMemId in self.mem

	def getSize(self):
		return [self.iCantVar[0], self.iCantVar[1], self.iCantVar[2], self.iCantVar[3]]

	def getSizeInt(self):
		return self.iCantVar[0]

	def getSizeReal(self):
		return self.iCantVar[1]

	def getSizeBool(self):
		return self.iCantVar[2]

	def getSizeString(self):
		return self.iCantVar[3]

	def getSizeType(self, iType):
		return self.iCantVar[iType]

	def getNextMem(self, iType):
		return self.iBaseVar[iType] + self.iCantVar[iType]
		
	def addVariable(self, iType, iValue=0, iSize=1):
		if iType == 3 and iValue == 0:
			iValue = ""
		iMem = self.getNextMem(iType)

		for i in range(0, iSize):
			self.mem[iMem + i] = iValue
		
		self.iCantVar[iType] = self.iCantVar[iType] + iSize
		if self.iBaseVar[iType] + self.getSizeType(iType) >= self.iLimit[iType]:
			return -1
		return iMem

	def getVariableValue(self, iMem):
		try:
			if int(iMem) in self.mem:
				return self.mem[int(iMem)]
			return None
		except :
			return None

	def setVariableValue(self, iMem, iValue):
		self.mem[iMem] = iValue
		return True

	def pprint(self):
		for iMem, iValue in self.mem.items():
			print(str(iMem) + ": " + str(iValue))


# ##################################################### #

class MemoryFunction:
	def __init__(self, iBaseVars, iCantVars, iBaseFunc, iCantFuncs):
		self.iBaseFuncIDs = iBaseFunc
		self.iLimitFunc = iBaseFunc + iCantFuncs

		iCantVar = iCantVars / 5
		self.iBaseVar = {}
		self.iLimit = {}
		for i in range(0, 4):
			self.iBaseVar[i] = iBaseVars + i * iCantVar
			self.iLimit[i] = iBaseVars + (i+1) * iCantVar

		iCantVar = iCantVars / 5

		self.mem = {}
	
	def exists(self, iMemId):
		return self.mem[self.iBaseFuncIDs].exists(iMemId)

	def getSize(self):
		return self.mem[self.iBaseFuncIDs].getSize()

	def getSizeInt(self):
		return self.mem[self.iBaseFuncIDs].getSizeInt()

	def getSizeReal(self):
		return self.mem[self.iBaseFuncIDs].getSizeReal()

	def getSizeBool(self):
		return self.mem[self.iBaseFuncIDs].getSizeBool()

	def getSizeString(self):
		return self.mem[self.iBaseFuncIDs].getSizeString()

	def addVariable(self, iType, iValue=0, iSize=1):
		self.pprint()
		return self.mem[self.iBaseFuncIDs].addVariable(iType, iValue, iSize)

	def createFunction(self):
		self.mem[self.iBaseFuncIDs] = MemoryTypes(self.iBaseVar, self.iLimit)
		return self.iBaseFuncIDs

	def endFunction(self):
		iBaseVars = self.getSize()

		for i in range(0, 4):
			self.iBaseVar[i] = self.iBaseVar[i] + iBaseVars[i] 
		self.iBaseFuncIDs += 1

		return self.iBaseFuncIDs < self.iLimitFunc

	def getLocal(self, iFuncID):
		return self.mem[iFuncID]

	def getVariableValue(self, iMem):
		return self.mem.getVariableValue(iMem)

	def setVariableValue(self, iMem, iValue):
		return self.mem.setVariableValue(iMemId, iValue)

	def pprint(self):
		print "Entre"
		for iFunID, Function in self.mem.items():
			print("Funcion " + str(iFunID) + ": ")
			self.mem[iFunID].pprint()
			print("")


# ##################################################### #
class MemoryGlobal:
	def __init__(self, iBaseVars, iCantVars):
		iCantVar = iCantVars / 5
		iBaseVar = {}
		iLimit = {}
		for i in range(0, 4):
			iBaseVar[i] = iBaseVars + i * iCantVar
			iLimit[i] = iBaseVars + (i+1) * iCantVar

		self.mem = MemoryTypes(iBaseVar, iLimit)

	def exists(self, iMemId):
		return self.mem.exists(iMemId)

	def getSize(self):
		return self.mem.getSize()

	def getSizeInt(self):
		return self.mem.getSizeInt()

	def getSizeReal(self):
		return self.mem.getSizeReal()

	def getSizeBool(self):
		return self.mem.getSizeBool()

	def getSizeString(self):
		return self.mem.getSizeString()

	def addVariable(self, iType, iValue=0, iSize=1):
		return self.mem.addVariable(iType, iValue, iSize)

	def getVariableValue(self, iMem):
		return self.mem.getVariableValue(iMem)

	def setVariableValue(self, iMem, iValue):
		return self.mem.setVariableValue(iMem, iValue)

	def pprint(self):
		self.mem.pprint()

# ##################################################### #


class MemoryConstante:
	def __init__(self, iBaseVars, iCantVars):
		iCantVar = iCantVars / 5
		iBaseVar = {}
		iLimit = {}
		for i in range(0, 4):
			iBaseVar[i] = iBaseVars + i * iCantVar
			iLimit[i] = iBaseVars + (i+1) * iCantVar

		self.mem = MemoryTypes(iBaseVar, iLimit)
		
	def exists(self, iMemId):
		return self.mem.exists(iMemId)

	def getSize(self):
		return self.mem.getSize()

	def getSizeInt(self):
		return self.mem.getSizeInt()

	def getSizeReal(self):
		return self.mem.getSizeReal()

	def getSizeBool(self):
		return self.mem.getSizeBool()

	def getSizeString(self):
		return self.mem.getSizeString()

	def addVariable(self, iType, iValue=0, iSize=1):
		return self.mem.addVariable(iType, iValue, iSize)

	def getVariableValue(self, iMem):
		return self.mem.getVariableValue(iMem)

	def setVariableValue(self, iMem, iValue):
		return self.mem.setVariableValue(iMemId, iValue)

	def pprint(self):
		self.mem.pprint()


# ##################################################### #

class MemoryManager:
	def __init__(self, memory):
		self.mem = memory

		self.globa = memory.getGlobal()
		self.function = {}
		self.constante = memory.getConstant()

		self.stNextFunction = Stack()
		self.stFunctions = Stack()

	def moveMemGoSub(self):
		self.stFunctions.push(self.function)
		self.function = self.stNextFunction.pop()

	def returnGoSub(self):
		self.function = self.stFunctions.pop()


	def eraFuncion(self, iFuncID):
		self.stNextFunction.push(copy.deepcopy(self.mem.getLocal(iFuncID)))

	def paramFunction(self, iMemId, iValue):
		stF = self.stNextFunction.pop()
		stF.setVariableValue(iMemId, iValue)
		self.stNextFunction.push(stF)

	def getVariableValue(self, iMemId):
		if self.globa.exists(iMemId):
			return self.globa.getVariableValue(iMemId)
		if self.function.exists(iMemId):
			return self.function.getVariableValue(iMemId)
		if self.constante.exists(iMemId):
			return self.constante.getVariableValue(iMemId)
		return None

	def setVariableValue(self, iMemId, iValue):
		if self.globa.exists(iMemId):
			return self.globa.setVariableValue(iMemId, iValue)
		if self.function.exists(iMemId):
			return self.function.setVariableValue(iMemId, iValue)
		if self.constante.exists(iMemId):
			return self.constante.setVariableValue(iMemId, iValue)
		return None
	
	def pprint(self):
		print(" ********** Memory ********** ")
		print("Globales: ")
		self.globa.pprint()
		print("\nFunciones: ")
		self.function.pprint()
		print("\nConstantes: ")
		self.constante.pprint()
		print(" **************************** ")


# ##################################################### #

class Memory:
	def __init__(self, iMemGlobal, iMemLocal, iMemCte):
		self.globa = MemoryGlobal(iMemGlobal[0], iMemGlobal[1])
		self.local = MemoryFunction(iMemLocal[0], iMemLocal[1], iMemLocal[2], iMemLocal[3])
		self.constante = MemoryConstante(iMemCte[0], iMemCte[1])

	def addVariableGlobal(self, iType, iValue=0, iSize=1):
		return self.globa.addVariable(iType, iValue, iSize)

	def addVariableLocal(self, iType, iValue=0, iSize=1):
		return self.local.addVariable(iType, iValue, iSize)

	def addVariableConstante(self, iType, iValue=0, iSize=1):
		return self.constante.addVariable(iType, iValue, iSize)

	def addVariableTemporal(self, iType, iValue=0, iSize=1):
		return self.local.addVariable(iType, iValue, iSize)

	def createFunction(self):
		return self.local.createFunction()

	def endFunction(self):
		return self.local.endFunction()

	def getGlobal(self):
		return self.globa

	def getConstant(self):
		return self.constante

	def getLocal(self, iFuncID):
		return self.local.getLocal(iFuncID)

	def getVariableValue(self, iMemId):
		if self.globa.exists(iMemId):
			return self.globa.getVariableValue(iMemId)
		if self.local.exists(iMemId):
			return self.function.getVariableValue(iMemId)
		if self.constante.exists(iMemId):
			return self.constante.getVariableValue(iMemId)
		return None

	def obtenValorCte(self, iMemId):
		return str(self.constante.getVariableValue(iMemId))

	def pprint(self):
		print(" ********** Memory ********** ")
		print("Globales: ")
		self.globa.pprint()
		print("\nFunciones: ")
		self.local.pprint()
		print("\nConstantes: ")
		self.constante.pprint()
		print(" **************************** ")


# ##################################################### #
"""
m = Memory([100000, 100000], [200000, 100000, 1000000, 10000], [300000, 100000])

print m.addVariableGlobal(0)
print m.addVariableGlobal(0)
print m.addVariableGlobal(1)
print m.addVariableGlobal(3)
print m.addVariableGlobal(2)
print m.addVariableGlobal(0, 0, 10)
print m.addVariableGlobal(0)

print m.addVariableConstante(0)
print m.addVariableConstante(2)

print m.createFunction()
print m.addVariableLocal(0)
print m.addVariableLocal(0)
print m.addVariableLocal(0)
print m.addVariableLocal(0)
print m.addVariableLocal(0)
print m.addVariableLocal(0, 0, 1000)
print m.addVariableLocal(0, 0, 2)
print m.addVariableLocal(0, 0, 1)

print m.addVariableLocal(1)
print m.addVariableLocal(1)
print m.addVariableLocal(1)
print m.addVariableLocal(2)
print m.addVariableLocal(2)
print m.addVariableLocal(1, 0, 1000)
print m.addVariableLocal(1, 0, 2)
print m.addVariableLocal(2, 0, 1)
print m.addVariableLocal(2, 0, 0)
print m.endFunction()

print "\n\n"

print m.createFunction()
print m.addVariableLocal(0)
print m.addVariableLocal(0)
print m.addVariableLocal(0)
print m.addVariableLocal(0)
print m.addVariableLocal(0)
print m.addVariableLocal(0, 0, 1000)
print m.addVariableLocal(0, 0, 2)
print m.addVariableLocal(0, 0, 1)

print m.addVariableLocal(1)
print m.addVariableLocal(1)
print m.addVariableLocal(1)
print m.addVariableLocal(2)
print m.addVariableLocal(2)
print m.addVariableLocal(1, 0, 1000)
print m.addVariableLocal(1, 0, 2)
print m.addVariableLocal(2, 0, 1)
print m.addVariableLocal(2, 0, 0)

m.pprint()
"""