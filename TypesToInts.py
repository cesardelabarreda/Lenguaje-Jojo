class TypeToInt:
	def __init__(self):
		self.types = {
      "int"     : 0,
      "real"    : 1,
      "bool"    : 2,
      "string"  : 3,
      "stand"   : 4,
      
      "public"  : 0,
      "private" : 1,

      "="       : 0,
      "+"       : 1,
      "-"       : 2,
      "*"       : 3,
      "/"       : 4,
      "%"       : 5,
      "<"       : 6,
      "<="      : 7,
      ">"       : 8,
      ">="      : 9,
      "=="      : 10,
      "!="      : 11,
      "&&"      : 12,
      "||"      : 13,
      "!"       : 14,
    }

	def exists(self, sType):
		return sType in self.types

	def convert(self, sType):
		if self.exists(sType) == 0:
			return -1
		return self.types[sType]