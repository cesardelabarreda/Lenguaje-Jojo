class TypeToInt:
	def __init__(self):
		self.types = {
  		"int" 		: 0,
  		"real" 	  : 1,
  		"bool"		: 2,
  		"string" 	: 3,
  		"stand"		: 4,
  		
      "public"	: 0,
  		"private"	: 1,

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

class SemanticCube:
  def __init__(self):
    self.cube = {}
    # Operador 1 - Operador - Operando 2
    
    # Int
    self.cube[0] = {}

    # Int =
    self.cube[0][0] = {}
    self.cube[0][0][0] = 0
    self.cube[0][0][1] = 0

    # Int +
    self.cube[0][1] = {}
    self.cube[0][1][0] = 0
    self.cube[0][1][1] = 1
    
    # Int -
    self.cube[0][2] = {}
    self.cube[0][2][0] = 0
    self.cube[0][2][1] = 1

    # Int *
    self.cube[0][3] = {}
    self.cube[0][3][0] = 0
    self.cube[0][3][1] = 1

    # Int /
    self.cube[0][4] = {}
    self.cube[0][4][0] = 0
    self.cube[0][4][1] = 1

    # Int %
    self.cube[0][5] = {}
    self.cube[0][5][0] = 0

    # Int <
    self.cube[0][6] = {}
    self.cube[0][6][0] = 2
    self.cube[0][6][1] = 2

    # Int <=
    self.cube[0][7] = {}
    self.cube[0][7][0] = 2
    self.cube[0][7][1] = 2

    # Int >
    self.cube[0][8] = {}
    self.cube[0][8][0] = 2
    self.cube[0][8][1] = 2

    # Int >=
    self.cube[0][9] = {}
    self.cube[0][9][0] = 2
    self.cube[0][9][1] = 2

    # Int ==
    self.cube[0][10] = {}
    self.cube[0][10][0] = 2
    self.cube[0][10][1] = 2

    # Int !=
    self.cube[0][11] = {}
    self.cube[0][11][0] = 2
    self.cube[0][11][1] = 2


    # Real 
    self.cube[1] = {}

    # Real =
    self.cube[1][0] = {}
    self.cube[1][0][0] = 1
    self.cube[1][0][1] = 1

    # Real +
    self.cube[1][1] = {}
    self.cube[1][1][0] = 1
    self.cube[1][1][1] = 1

    # Real -
    self.cube[1][2] = {}
    self.cube[1][2][0] = 1
    self.cube[1][2][1] = 1

    # Real *
    self.cube[1][3] = {}
    self.cube[1][3][0] = 1
    self.cube[1][3][1] = 1

    # Real /
    self.cube[1][4] = {}
    self.cube[1][4][0] = 1
    self.cube[1][4][1] = 1

    # Real <
    self.cube[1][6] = {}
    self.cube[1][6][0] = 2
    self.cube[1][6][1] = 2

    # Real <=
    self.cube[1][7] = {}
    self.cube[1][7][0] = 2
    self.cube[1][7][1] = 2

    # Real >
    self.cube[1][8] = {}
    self.cube[1][8][0] = 2
    self.cube[1][8][1] = 2

    # Real >=
    self.cube[1][9] = {}
    self.cube[1][9][0] = 2
    self.cube[1][9][1] = 2

    # Real ==
    self.cube[1][10] = {}
    self.cube[1][10][0] = 2
    self.cube[1][10][1] = 2

    # Real !=
    self.cube[1][11] = {}
    self.cube[1][11][0] = 2
    self.cube[1][11][1] = 2



    # Bool 
    self.cube[2] = {}

    # Bool =
    self.cube[2][0] = {}
    self.cube[2][0][2] = 2
    self.cube[2][0][2] = 2

    # Bool ==
    self.cube[2][10] = {}
    self.cube[2][10][2] = 2
    self.cube[2][10][2] = 2

    # Bool !=
    self.cube[2][11] = {}
    self.cube[2][11][2] = 2
    self.cube[2][11][2] = 2

    # Bool &&
    self.cube[2][12] = {}
    self.cube[2][12][2] = 2
    self.cube[2][12][2] = 2

    # Bool ||
    self.cube[2][13] = {}
    self.cube[2][13][2] = 2
    self.cube[2][13][2] = 2

    # Bool !
    self.cube[2][14] = 2


    # String 
    self.cube[3] = {}

    # String =
    self.cube[3][0] = {}
    self.cube[3][0][3] = 3
    
    # String +
    self.cube[3][1] = {}
    self.cube[3][1][3] = 3

  def exists(self, opLeft, opRight, op):
    if opLeft in self.cube:
        if op in self.cube[opLeft]:
            return opRight in self.cube[opLeft][op]
    return False