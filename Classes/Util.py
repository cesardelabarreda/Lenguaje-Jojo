from __future__ import print_function
import pprint
import sys

class Error:
	def __init__(self):
		self.cantErrors = 0
		self.error = [
			"Error sintactico, token no esperado.", 	      # 0
			"Redefinicion de Atributo ya existente.",	      # 1
			"Redefinicion de Variable ya existente.",       # 2
			"Redefinicion de Funcion ya existente.",        # 3
			"Redefinicion de Metodo ya existente.", 		    # 4
			"Redefinicion de Clase ya existente.",          # 5	
			"Se intento heredar de Clase no declarada.",    # 6
			"Error sintactico, Tipo de datos no compatibles", # 7
			"Variable no declarada",                        # 8
			"Type mismatch",                                # 9
			"Se esperaba token",                            # 10
			"Tipo de retorno equivocado",										# 11
		]

	def printError(self, errorId, message, lineNo):
		self.cantErrors = self.cantErrors + 1
		sys.stderr.write("ID-Error %d: %s\n%s\nLinea: %d\n\n" %(self.cantErrors, self.error[errorId], message, lineNo))

	def hasError(self):
		return self.cantErrors != 0


class Util:
	def printDicClass(self, dictionaryClass):
		print(" ********** dictionaryClass ********** ")
		dictionaryClass.pprint()
		print(" ************************************* \n\n\n\n")

	def printDicFunctions(self, dictionaryFunctions):
		print(" ********** dictionaryFunctions ********** ")
		dictionaryFunctions.pprint()
		print(" ***************************************** \n\n\n\n")

	def printQuadruples(self, quads):
		print(" ********** quads ********** ")
		quads.pprint()
		print(" ***************************************** \n\n\n\n")

	def printStackID(self, stID):
		print(" ********** quads ********** ")
		#stID.Pprint()
		print(" ***************************************** \n\n\n\n")

	def printAll(self, dictionaryClass, dictionaryFunctions, quads, stID=None, stOper=None, stSaltos=None):
		self.printDicClass(dictionaryClass)
		self.printDicFunctions(dictionaryFunctions)
		self.printQuadruples(quads)
		self.printStackID(stID)

	def debug(self, args, lineNo, codeLineNo=None):
		for arg in args:
			print(arg), 
			print("  "),
		print("\nAt line: " + str(lineNo) + "\t\tCodeLine: " + str(codeLineNo))

	def eprint(*args, **kwargs):
		print(*args, file=sys.stderr, **kwargs)