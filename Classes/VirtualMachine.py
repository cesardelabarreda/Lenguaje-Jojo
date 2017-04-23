
from Memoria import Memory
from Cuadruplo import Quadruple
from Stack import Stack

global contQuads
global ret
global stEjecucion
stEjecucion = Stack()
contQuads = 0

dirMethods = {
	'+' : add
	'-' : subs
	'*' : mult
	'/' : div
	'%' : mod
	'<' : lessthan
	'>' : greaterthan
	'<=' : lessequals
	'>=' : greaterequals
	'goto' : goto
	'gotof' : gotof
	'gotov' : gotov
	'=' : equal
	'==' : equals
	'!=' : notequals
	'!' : nots
	'&&' : ands
	'||' : ors
	'gets' : gets
	'prints' : prints
	'era' : era
	'endProc' : endProc
	'param' : param
	'return' : returns
	'gosub' : gosub
}

class VM:
	def __init__(self, mapmemory, listCuadr):
		self.cuadruplo = {}
		self.mapmemory = {}
		self.pEjecucion = Stack()

	def add(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			if(mapmemory.exists(oper2)):
				Operando2 = mapmemory.get(oper2)
				mapmemory.insert(res, Operando1 + Operando2)
				return 1
		return 0

	def subs(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			if(mapmemory.exists(oper2)):
				Operando2 = mapmemory.get(oper2)
				mapmemory.insert(res, Operando1 - Operando2)
				return 1
		return 0

	def mult(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			if(mapmemory.exists(oper2)):
				Operando2 = mapmemory.get(oper2)
				mapmemory.insert(res, Operando1 * Operando2)
				return 1
		return 0

	def div(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			if(mapmemory.exists(oper2)):
				Operando2 = mapmemory.get(oper2)
				mapmemory.insert(res, Operando1 / Operando2)
				return 1
		return 0


	def mod(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			if(mapmemory.exists(oper2)):
				Operando2 = mapmemory.get(oper2)
				mapmemory.insert(res, Operando1 % Operando2)
				return 1
		return 0

	def ands(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			if(mapmemory.exists(oper2)):
				Operando2 = mapmemory.get(oper2)
				mapmemory.insert(res, Operando1 && Operando2)
				return 1
		return 0

	def ors(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			if(mapmemory.exists(oper2)):
				Operando2 = mapmemory.get(oper2)
				mapmemory.insert(res, Operando1 || Operando2)
				return 1
		return 0

	def nots(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			mapmemory.insert(res, not Operando1)
			return 1
		return 0


	def equal(self, oper1, oper2, res):
		if(mapmemory.exists(oper1)):
			Operando1 = mapmemory.get(oper1)
			mapmemory.insert(res, Operando1)
			return 1
	return 0

def notequals(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		Operando1 = mapmemory.get(oper1)
		if(mapmemory.exists(oper2)):
			Operando2 = mapmemory.get(oper2)
			mapmemory.insert(res, Operando1 != Operando2)
			return 1
	return 0

def greaterequals(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		Operando1 = mapmemory.get(oper1)
		if(mapmemory.exists(oper2)):
			Operando2 = mapmemory.get(oper2)
			mapmemory.insert(res, Operando1 >= Operando2)
			return 1
	return 0

def lessequals(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		Operando1 = mapmemory.get(oper1)
		if(mapmemory.exists(oper2)):
			Operando2 = mapmemory.get(oper2)
			mapmemory.insert(res, Operando1 >= Operando2)
			return 1
	return 0


def equals(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		Operando1 = mapmemory.get(oper1)
		if(mapmemory.exists(oper2)):
			Operando2 = mapmemory.get(oper2)
			mapmemory.insert(res, Operando1 == Operando2)
			return 1
	return 0

def greaterthan(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		Operando1 = mapmemory.get(oper1)
		if(mapmemory.exists(oper2)):
			Operando2 = mapmemory.get(oper2)
			mapmemory.insert(res, Operando1 > Operando2)
			return 1
	return 0


def lessthan(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		Operando1 = mapmemory.get(oper1)
		if(mapmemory.exists(oper2)):
			Operando2 = mapmemory.get(oper2)
			mapmemory.insert(res, Operando1 < Operando2)
			return 1
	return 0

def prints(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		Operando1 = mapmemory.get(oper1)
		print(Operando1)
		return 1
	return 0

def gets(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		Operando1 = raw_input()
		# Hay que checar que sea el tipo de entrada igual al tipo de dato
		mapmemory.insert(oper1, Operando1)
		return 1
	return 0


def goto(self, oper1, oper2, res):
	global contQuads
	contQuads = res
	return 1


def gotoF(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		if(not mapmemory.get(oper1)):   
			global contQuads
			contQuads = res
			return 1
	return 0

def gotoV(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		if(mapmemory.get(oper1)):   
			global contQuads
			contQuads = res
			return 1
	return 0




def era(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		mapmemory.era(oper1)
		return 1
	return 0


def param(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)): 
		mapmemory.param(oper1)
		return 1
	return 0

def returns(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		global ret
		ret = mapmemory.get(oper1)
		mapmemry.endProc()
		global contQuads
		contQuads = stEjecucion.pop
		return 1
	return 0

def gosub(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)): 
		global contQuads
		stEjecucion.push(contQuads)
		contQuads = res
		return 1
	return 0


def endProc(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		mapmemory.endProc()
		global contQuads
		contQuads = stEjecucion.pop
		return 1
	return 0


def run(self):
	while(contQuads < self.contQuads.size()):
		quad = self.contQuads.quads[contQuads]
		contQuads += 1
		Operando1 = quad[1]
		Operando2 = quad[2]
		Res = quad[3]
		self.dirMethods[quad[0]](Operando1, Operando2, Res)

