import copy
import sys
from Util import Util
from CuboSemantico import TypeConvertion
from DataStructures.Dictionary import Dictionary
from DataStructures.Stack import Stack
"""
	Clase MemoryTypes:
		Es lo mas abajo y base que hay de memoria. Separa en 4 tipos todo. Tiene la cantidad
			de variables que van de cada tipo, los limites y las bases, ademas de la memoria en si.

		El atributo iBaseVar un mapa que guarda cual es la direccion base de cada uno de los tipos.
			La llave es el tipo de dato.
		El atributo iCantVar es un mapa que tiene como llave el tipo de dato y guarda la cantidad
			de variables que se estan usando.
		El atributo iLimit es un mapa que tiene como llave el tipo de dato y guarda el maximo valor
			que se puede llegar a tener en memoria.
"""

"""
	Clase MemoryFunction:
		Es lo mas abajo y base que hay de memoria. Separa en 4 tipos todo. Tiene la cantidad
			de variables que van de cada tipo, los limites y las bases, ademas de la memoria en si.

		El atributo iBaseVar un mapa que guarda cual es la direccion base de cada uno de los tipos.
			La llave es el tipo de dato.
		El atributo iCantVar es un mapa que tiene como llave el tipo de dato y guarda la cantidad
			de variables que se estan usando.
		El atributo iLimit es un mapa que tiene como llave el tipo de dato y guarda el maximo valor
			que se puede llegar a tener en memoria.
"""

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
	
	# Cada vez que se va a agregar un arreglo o una variable, se llega a este metodo
	# 	el cual se encarga de asignar un valor default en memoria (en caso de que)
	# 	no se le de un valor, para los n valores que se le de (iSize). En caso de
	# 	que se exceda el tamano maximo, se marca un mensaje de error.
	def addVariable(self, iType, iValue=0, iSize=1):
		if iType == 3 and iValue == 0:
			iValue = ""
		iMem = self.getNextMem(iType)

		for i in range(0, iSize):
			self.mem[iMem + i] = iValue
		
		self.iCantVar[iType] = self.iCantVar[iType] + iSize
		if self.iBaseVar[iType] + self.getSizeType(iType) >= self.iLimit[iType]:
			print "Limite de memoria excedido"
			print "ReturnType -1"
			sys.exit()
			return -1
		return iMem

	def getVariableValue(self, iMem):
		try:
			if int(iMem) in self.mem:
				return self.mem[int(iMem)]
			return None
		except:
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
		return self.mem[self.iBaseFuncIDs].addVariable(iType, iValue, iSize)

	# Cada vez que se crea una funcion, se genera un nuevo ID y se crea el espacio
	# 	de memoria para esa localidad. Si la cantidad de funciones posibles a declarar
	#		excede el limite, el programa termina con error.
	def createFunction(self):
		if self.iBaseFuncIDs == 1010000:
			print "Limite de memoria excedido"
			print "ReturnType -1"
			sys.exit()
		self.mem[self.iBaseFuncIDs] = MemoryTypes(self.iBaseVar, self.iLimit)
		return self.iBaseFuncIDs

	# Cada vez que se termina de procesar una funcion, se marca como finalizada esa
	#		funcion y se agrega 1 a la cantidad de funciones totales que se tienen.
	# 	Tambien se actualizan los rangos para que las proximas funciones puedan ser
	# 	creadas con exactitud
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

	# Cuando se llama a un gosub, se guarda en la pila de funciones la memoria
	# 	que se esta usando actualmente como local/funcion. Ademas, se saca de la
	# 	pila de nextfunctions la siguiente funcion a usar. 
	def moveMemGoSub(self):
		self.stFunctions.push(self.function)
		self.function = self.stNextFunction.pop()

	# Cuando se termina una funcion, se obtiene de vuelta la ultima memoria de funcion
	# 	que se guardo en la pila, de esta forma puede continuar donde quedo ejecutand.
	def returnGoSub(self):
		self.function = self.stFunctions.pop()

	# Cuando hay un ERA, se mete a la pila de siguientes funciones una copia de la
	#		funcion a la cual se va a mover ahora la ejecusion.
	def eraFuncion(self, iFuncID):
		self.stNextFunction.push(copy.deepcopy(self.mem.getLocal(iFuncID)))

	# Cuando hay un param, se asigna el valor de en memoria a la ultima funcion que
	# 	se le creo el era.
	def paramFunction(self, iMemId, iValue):
		stF = self.stNextFunction.pop()
		stF.setVariableValue(iMemId, iValue)
		self.stNextFunction.push(stF)

	# Obtiene un valor dada un Id de memoria.
	def getVariableValue(self, iMemId):
		if self.globa.exists(iMemId):
			return self.globa.getVariableValue(iMemId)
		if self.function.exists(iMemId):
			return self.function.getVariableValue(iMemId)
		if self.constante.exists(iMemId):
			return self.constante.getVariableValue(iMemId)
		return None

	# Se asigna un valor dada un Id de memoria.
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