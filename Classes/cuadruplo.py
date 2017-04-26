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

	def pprint(self):
		typeConv = TypeConvertion()
		iNum = 0
		for quad in self.quads:
			print(str(iNum) + "\t["),
			print(str(typeConv.convertOp(quad[0]))),
			for i in range(1, 4):
				print(str("\t")),
				print(str(quad[i])),
			print("]")
			iNum = iNum + 1