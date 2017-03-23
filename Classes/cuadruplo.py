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

	def fill(self, quadNum, filler):
		if self.size() <= quadNum:
			return 0
		if self.size() <= filler:
			return 0
		self.quads[quadNum][3] = filler
		return 1