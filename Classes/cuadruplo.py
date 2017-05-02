import sys
import pprint
from CuboSemantico import TypeConvertion

class Quadruple:
	def __init__(self):
		self.quads = []

	def empty(self):
		return self.empty == []

	def size(self):
		return len(self.quads)

	def clear(self):
		self.quads = []

	def append(self, operation, left=None, right=None, temp=None):
		self.quads.append([operation, left, right, temp])

	def fill(self, quadNum, filler, fillPos=3):
		if self.size() <= quadNum:
			return 0
		self.quads[quadNum][fillPos] = filler
		return 1

	def pprint(self, dicFunc, mem):
		typeConv = TypeConvertion()
		iNum = 0
		for quad in self.quads:
			print(str(iNum) + "\t["),
			
			print(str(typeConv.convertOp(quad[0]))),
			iTam = len(str(typeConv.convertOp(quad[0])))
			for j in range(0, 3):
				print(" "),

			for i in range(1, 4):
				if quad[i] == None:
					print(str(quad[i])),
					iTam = 14 - len(str(quad[i]))
					if (iTam % 2 == 1):
						iTam = iTam - 3
						print("  "),
					for j in range(0, (iTam / 2)):
						print(" "),
				else:
					sVal = str(dicFunc.buscaVar(quad[i]))
					if str(sVal) == str(None):
						sVal = mem.obtenValorCte(quad[i])
						if str(sVal) == str(None):
							sVal = quad[i]

					print(str(sVal)),
					iTam = 14 - len(str(sVal))
					if (iTam % 2 == 1):
						iTam = iTam - 3
						print("  "),
					for j in range(0, (iTam / 2)):
						print(" "),
			print("]")
			iNum = iNum + 1

	def pprint2(self):
		typeConv = TypeConvertion()
		iNum = 0
		for quad in self.quads:
			print(str(iNum) + "\t["),
			
			print(str(typeConv.convertOp(quad[0]))),
			iTam = len(str(typeConv.convertOp(quad[0])))
			for j in range(0, 3):
				print(" "),

			for i in range(1, 4):
				if quad[i] == None:
					print(str(quad[i])),
					iTam = 14 - len(str(quad[i]))
					if (iTam % 2 == 1):
						iTam = iTam - 3
						print("  "),
					for j in range(0, (iTam / 2)):
						print(" "),
				else:
					print(str(quad[i])),
					iTam = 14 - len(str(sVal))
					if (iTam % 2 == 1):
						iTam = iTam - 3
						print("  "),
					for j in range(0, (iTam / 2)):
						print(" "),
			print("]")
			iNum = iNum + 1