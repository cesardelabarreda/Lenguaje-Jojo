class TypeToInt:
	def __init__(self):
		self.types = {
  		"int" 		: 0,
  		"double" 	: 1,
  		"bool"		: 2,
  		"string" 	: 3,
  		"obj"			: 4,
  		"public"	: 0,
  		"private"	: 1,
  		"func"		: 0,
  	}

	def exists(self, sType):
		return sType in self.types

	def convert(self, sType):
		if self.exists(sType) == 0:
			return -1
		return self.types[sType]