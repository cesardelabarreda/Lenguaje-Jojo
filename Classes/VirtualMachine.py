
from Memoria import Memory
from Cuadruplo import Quadruple
from Stack import Stack

global contQuads
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


def goto(self, oper1, oper2, res):
	global contQuads
	contQuads = res
	return 1


def gotov(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		if(mapmemory.get(not oper1)):   
			global contQuads
			contQuads = res
			return 1
	return 0

def gotov(self, oper1, oper2, res):
	if(mapmemory.exists(oper1)):
		if(mapmemory.get(oper1)):   
			global contQuads
			contQuads = res
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

