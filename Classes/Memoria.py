from Util import Util
from CuboSemantico import TypeConvertion
from DataStructures.Dictionary import Dictionary
from DataStructures.Stack import Stack

class MemoryTypes:
	def __init__(self, iBaseVars):
		self.count = {}

		for i in range(0, 4):
			self.iBaseVar[i] = iBaseVars[i]
			self.iCantVar[i] = 0

		self.mem = {}

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
		return iBaseVar[iType] + iCantVar[iType]
		
	def addVariable(self, iType, iValue=0, iSize=1):
		if iType == 3:
			iValue = ""
		iMem = self.getNextMem(iType)

		for i in range(0, iSize):
			self.mem[iMem] = iValue
		
		self.count[iMem] = self.count[iMem] + iSize
		return iMem

	def getVariableValue(self, iMem):
		return self.mem[iMem]


# ##################################################### #

class MemoryFunction:
	def __init__(self, iBaseFunc, iBaseVars):
		self.mem = {}
		MemoryTypes()

		self.iBaseFuncIDs = iBaseFunc

		for i in range(0, 4):
			self.iBaseVar[i] = iBaseVars[i]

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
		self.mem[self.iBaseFuncIDs] = MemoryTypes(self.iBaseVar)
		return self.iBaseFuncIDs

	def endFunction(self):
		iBaseVars = self.getSize(self.iBaseFuncIDs)

		for i in range(0, 4):
			self.iBaseVar[i] = iBaseVars[i] 
		self.iBaseFuncIDs += 1

	def getVariableValue(self, iMem):
		return self.mem.getVariableValue(iMem)


# ##################################################### #
class MemoryGlobal:
	def __init__(self, iBaseVars):
		self.mem = MemoryTypes(iBaseVars)

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
		self.mem.getVariableValue(iMem)

# ##################################################### #


class MemoryConstante:
	def __init__(self, iBaseVars):
		self.mem = MemoryTypes()

		for i in range(0, 4):
			self.iBaseVar[i] = iBaseVars[i]

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
		self.mem.getVariableValue(iMem)


# ##################################################### #

class MemoryManager:
	def __init__(self, memory):
		self.mem = memory

		self.globa = memory.getGlobal()
		self.function = {}
		self.constante = memory.getConstant()

		self.nextFunction = {}
		self.quFunctions = Queue()

	def moveMemGoSub(self):
		self.quFunction.push(self.function)
		self.function = self.nextFunction

	def returnGoSub(self):
		self.function = quLocales.pop()

	def eraLocal(self, iFuncID):
		self.nextFunction = memory.getLocal(iFuncID)

	def getVariableValue(self, iMemId):
		if self.globa.exists(iMemId):
			return self.globa.getVariableValue(iMemId)
		if self.function.exists(iMemId):
			return self.function.getVariableValue(iMemId)
		if self.constante.exists(iMemId):
			return self.constante.getVariableValue(iMemId)
		return None


class Memory:
	def __init__(self):
		self.globa = MemoryGlobal()
		self.local = MemoryFunction()
		self.constante = MemoryConstante()

	def addVariableGlobal(self, iType, iSize=1):
		return self.mem["global"].addVariable(iType, iSize)

	def addVariableLocal(self, iType, iSize=1):
		return self.mem["local"].addVariable(iType, iSize)

	def addVariableTemporal(self, iType, iValue):
		return self.mem["temporal"].addVariable(iType, iValue)

	def addVariableConstante(self, iValue):
		return self.mem["constante"].addVariable(iType, iValue)