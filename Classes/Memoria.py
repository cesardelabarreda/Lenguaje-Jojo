from Util import Util
from CuboSemantico import TypeConvertion
from DataStructures.Dictionary import Dictionary
from DataStructures.Stack import Stack

class MemoryTypes:
	def __init__(self, iBaseVars, iCantVars):
		iCantVars /= 5

		self.iBaseVar = {}
		self.iCantVar = {}
		for i in range(0, 4):
			self.iBaseVar[i] = iBaseVars + (i * iCantVars)
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

	def getNextMem(self, iType):
		return self.iBaseVar[iType] + self.iCantVar[iType]
		
	def addVariable(self, iType, iValue=0, iSize=1):
		if iType == 3:
			iValue = ""
		iMem = self.getNextMem(iType)

		for i in range(0, iSize):
			self.mem[iMem] = iValue
		
		self.iCantVar[iType] = self.iCantVar[iType] + iSize
		return iMem

	def getVariableValue(self, iMem):
		return self.mem[iMem]

	def setVariableValue(self, iMem, iValue):
		self.mem.setVariableValue(iMemId, iValue)
		return True


# ##################################################### #

class MemoryFunction:
	def __init__(self, iBaseFunc, iBaseVars, iCantVars):
		self.mem = {}

		self.iBaseFuncIDs = iBaseFunc

		iCantVars /= 4

		self.iBaseVar = {}
		for i in range(0, 4):
			self.iBaseVar[i] = iBaseVars + (i * iCantVars)
	
	def exists(self, iMemId):
		return self.mem.exists(iMemId)

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
		return self.mem[self.iBaseFuncIDs].addVariable(iType, iValue, iSize)

	def createFunction(self):
		self.mem[self.iBaseFuncIDs] = MemoryTypes(self.iBaseVar[0], 10000)
		return self.iBaseFuncIDs

	def endFunction(self):
		iBaseVars = self.getSize(self.iBaseFuncIDs)

		for i in range(0, 4):
			self.iBaseVar[i] = iBaseVars[i] 
		self.iBaseFuncIDs += 1

	def getVariableValue(self, iMem):
		return self.mem.getVariableValue(iMem)

	def setVariableValue(self, iMem, iValue):
		return self.mem.setVariableValue(iMemId, iValue)


# ##################################################### #
class MemoryGlobal:
	def __init__(self, iBaseVars, iCantVars):
		self.mem = MemoryTypes(iBaseVars, iCantVars)

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

# ##################################################### #


class MemoryConstante:
	def __init__(self, iBaseVars, iCantVar):
		self.mem = MemoryTypes(iBaseVars, iCantVar)

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
		self.mem.addVariable(iType, iValue, iSize)

	def getVariableValue(self, iMem):
		return self.mem.getVariableValue(iMem)

	def setVariableValue(self, iMem, iValue):
		return self.mem.setVariableValue(iMemId, iValue)


# ##################################################### #

class MemoryManager:
	def __init__(self, memory):
		self.mem = memory

		self.globa = memory.getGlobal()
		self.function = {}
		self.constante = memory.getConstant()

		self.quNextFunction = Queue()
		self.quFunctions = Queue()

	def moveMemGoSub(self):
		self.quFunction.push(self.function)
		self.function = self.quNextFunction.pop()

	def returnGoSub(self):
		self.function = quLocales.pop()

	def eraFuncion(self, iFuncID):
		self.quNextFunction.push(memory.getLocal(iFuncID))

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

# ##################################################### #

class Memory:
	def __init__(self, iMemGlobal, iMemLocal, iMemCte):
		self.globa = MemoryGlobal(iMemGlobal[0], iMemGlobal[1])
		self.local = MemoryFunction(iMemLocal[0], iMemLocal[1], iMemLocal[2])
		self.constante = MemoryConstante(iMemCte[0], iMemCte[1])

	def addVariableGlobal(self, iType, iValue=0, iSize=1):
		return self.globa.addVariable(iType, iValue, iSize)

	def addVariableLocal(self, iType, iValue=0, iSize=1):
		return self.local.addVariable(iType, iValue, iSize)

	def addVariableConstante(self, iType, iValue=0, iSize=1):
		return self.constante.addVariable(iType, iValue, iSize)

	def createFunction(self):
		return self.local.createFunction()

	def endFunction(self):
		return self.local.endFunction()


# ##################################################### #

m = Memory([100000, 100000], [1000000, 200000, 100000], [300000, 100000])

print m.addVariableGlobal(0)
print m.addVariableGlobal(0)
print m.addVariableGlobal(1)
print m.addVariableGlobal(3)
print m.addVariableGlobal(2)
print m.addVariableGlobal(0, 0, 10)
print m.addVariableGlobal(0)

print m.createFunction()
m.addVariableLocal()
