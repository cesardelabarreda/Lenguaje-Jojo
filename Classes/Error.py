
class Error:
  def __init__(self):
    self.cantErrors = 0
    self.error = [
  		"Error sintactico, token no esperado.", 	   # 0
			"Redefinicion de Atributo ya existente.",	   # 1
			"Redefinicion de Variable ya existente.",    # 2
			"Redefinicion de Funcion ya existente.",     # 3
			"Redefinicion de Metodo ya existente.", 		 # 4
			"Redefinicion de Clase ya existente.",		   # 5	
      "Se intento heredar de Clase no declarada.", # 6
  	]
    

  def printError(self, errorId, message, lineNo):
    print("Error %d: %s\n%s\nLinea: %d\n\n" %(errorId, self.error[errorId], message, lineNo))
    self.cantErrors = self.cantErrors + 1