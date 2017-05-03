
from Memoria import MemoryManager
from Memoria import Memory
from Cuadruplo import Quadruple
from DataStructures.Stack import Stack

global contQuads
global objeto
objeto = Stack()
global ret
contQuads = 0



class VM:
	def __init__(self, mapMem, listCuadr):
		self.cuadruplo = listCuadr
		self.mapmemory = MemoryManager(mapMem)
		self.stEjecucion = Stack()

	def add(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 + Operando2)
			return 1
		return 0

	def subs(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 - Operando2)
			return 1
		return 0

	def mult(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 * Operando2)
			return 1
		return 0

	def div(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 / Operando2)
			return 1
		return 0


	def mod(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 % Operando2)
			return 1
		return 0

	def ands(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 and Operando2)
			return 1
		return 0

	def ors(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 or Operando2)
			return 1
		return 0

	def nots(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		if Operando1 != None :
			self.mapmemory.setVariableValue(res, not Operando1)
			return 1
		return 0


	def equal(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		if Operando1 != None :
			self.mapmemory.setVariableValue(res, Operando1)
			return 1
		else:
			global ret
			self.mapmemory.setVariableValue(res, ret)
			return 1
		return 0

	def notequals(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 != Operando2)
			return 1
		return 0

	def greaterequals(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 >= Operando2)
			return 1
		return 0

	def lessequals(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 <= Operando2)
			return 1
		return 0


	def equals(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 == Operando2)
			return 1
		return 0

	def greaterthan(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 > Operando2)
			return 1
		return 0


	def lessthan(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		Operando2 = self.mapmemory.getVariableValue(oper2)
		if Operando1 != None and Operando2 != None :
			self.mapmemory.setVariableValue(res, Operando1 < Operando2)
			return 1
		return 0

	def prints(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		if Operando1 != None :
			print(Operando1)
			return 1
		return 0

	def gets(self, oper1, oper2, res):
		Operando1 = raw_input()
		if oper2 == 0 :
			try:
				Operando1 = int(Operando1)
			except ValueError:
				return 0

		if oper2 == 1 :
			try:
				Operando1 = float(Operando1)
			except ValueError:
				return 0

		if oper2 == 2 :
			if Operando1 == "0":
				Operando1 = False
			else:
				Operando1 = True

		self.mapmemory.setVariableValue(oper1, Operando1)
		return 1


	def goto(self, oper1, oper2, res):
		global contQuads
		contQuads = res
		return 1


	def gotoF(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		if Operando1 != None :
			if not self.mapmemory.getVariableValue(oper1) :   
				global contQuads
				contQuads = res
			return 1
		return 0

	def gotoV(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		if Operando1 != None :
			if self.mapmemory.getVariableValue(oper1) :   
				global contQuads
				contQuads = res
			return 1
		return 0


	def era(self, oper1, oper2, res):
		self.mapmemory.eraFuncion(oper1)
		return 1


	def param(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		if Operando1 != None :
			self.mapmemory.paramFunction(res, Operando1)
			return 1
		return 0

	def returns(self, oper1, oper2, res):
		global ret
		global objeto
		if type(oper1) is list:
			ret = self.mapmemory.getVariableValue(oper1[1])
			listRet = oper1[0]
			for i in range(len(listRet)):
				oper1[0][i] = self.mapmemory.getVariableValue(listRet[i])
		
			self.mapmemory.returnGoSub()
			listobj = objeto.pop()
			for i in range(len(listRet)):
				self.mapmemory.setVariableValue(listobj[i], oper1[0][i])
			global contQuads
			contQuads = self.stEjecucion.pop()
			return 1
		else:
			ret = self.mapmemory.getVariableValue(oper1)
			if ret != None :		
				self.mapmemory.returnGoSub()
				global contQuads
				contQuads = self.stEjecucion.pop()
				return 1
		return 1

	def gosub(self, oper1, oper2, res):
		self.mapmemory.moveMemGoSub() 
		global contQuads
		self.stEjecucion.push(contQuads)
		contQuads = res
		return 1


	def endProc(self, oper1, oper2, res):
		self.mapmemory.returnGoSub()
		global contQuads
	 	contQuads = self.stEjecucion.pop()
		return 1

	def ver(self, oper1, oper2, res):
		Operando1 = self.mapmemory.getVariableValue(oper1)
		if Operando1 != None :
			if Operando1 >= oper2 and Operando1 <= res:
				return 1
		return 0

	def end(self, ope1, oper2, res):
		global contQuads
		contQuads = self.cuadruplo.size()




	global dirMethods
	dirMethods = {
		0	: equal,
		1 : add,
		2 : subs,
		3 : mult,
		4 : div,
		5 : mod,
		6 : lessthan,
		7 : lessequals,
		8 : greaterthan,
		9 : greaterequals,
		10 : equals,
		11 : notequals,
		12 : ands,
		13 : ors,
		14 : nots,
		15 : gets,
		16 : prints,
		17 : goto,
		18 : gotoF,
		19 : gotoV,
		20 : returns,
		21 : endProc,
		22 : era,
		23 : param,
		24 : gosub,
		25 : end,
		26 : ver,
	}

	def run(self):
		global contQuads
		global dirMethods
		global objeto
		while(contQuads < self.cuadruplo.size()):
			# print contQuads
			quad = self.cuadruplo.quads[contQuads]
			if quad[0] == 27:
				objeto.push(quad[1])
				contQuads += 1
				quad = self.cuadruplo.quads[contQuads]
			contQuads += 1
			Operando1 = quad[1]
			if type(Operando1) is list and quad[0] !=20:
				Operando1 = self.mapmemory.getVariableValue(Operando1[0])
			Operando2 = quad[2]
			if type(Operando2) is list :
				Operando2 = self.mapmemory.getVariableValue(Operando2[0])
			Res = quad[3]
			if type(Res) is list :
				Res = self.mapmemory.getVariableValue(Res[0])
			
			
			functionToCall = dirMethods[quad[0]]
			if functionToCall(self, Operando1, Operando2, Res) == 0:
				print "Error en cuadruplo "  + str(contQuads)
			"""
			try:
				print "Val 1: " + str(self.mapmemory.getVariableValue(Operando1))
				print "Val 2: " + str(self.mapmemory.getVariableValue(Operando2))
			except :
				print "hola"
			"""
