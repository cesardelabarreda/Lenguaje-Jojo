from Funcion import Function

class DicFunction:
  def __init__(self):
    f = Function(4)
    self.functions = {
      "_Global" : f,
    }

  def empty(self):
    return self.functions == {}

  def size(self):
    return len(self.functions)

  def clear(self):
    self.functions.clear()

  def clearFunctionVars(self, functionId):
    if self.existsFunction(functionId):
      self.functions[functionId].clearVars()

  def clearFunctionParams(self, functionId):
    if self.existsFunction(functionId):
      self.functions[functionId].clearParams()

  def clearFunction(self, functionId):
    if self.existsFunction(functionId):
      self.functions[functionId].clear()

  def deleteFunctionVar(self, functionId, varId):
    if self.existsFunction(functionId) == 0:
      return 0 
    return self.functions[functionId].deleteVar(varId)

  def deleteFunction(self, functionId):
    if self.existsFunction(functionId) == 0:
      return 0 
    del self.functions[functionId]
    return 1

  def existsFunction(self, functionId):
    return functionId in self.functions

  def existsVar(self, functionId, varId):
    if self.existsFunction(functionId):
      if self.functions[functionId].existsVar(varId):
        return 1
    return self.functions["_Global"].existsVar(varId)

  def insertFunction(self, functionId, functionRetType):
    if self.existsFunction(functionId):
      return 0

    func = Function(functionRetType)
    self.functions[functionId] = func
    return 1

  def insertVar(self, functionId, varId, varType):
    if self.existsFunction(functionId) == 0:
      return 0
    return self.functions[functionId].insertVar(varId, varType)

  def insertParam(self, functionId, varId, paramType):
    if self.existsFunction(functionId) == 0:
      return 0
    return self.functions[functionId].insertParam(varId, paramType)

  def getVariableType(self, functionId, varId):
    if self.existsFunction(functionId):
      tipo = self.functions[functionId].getVariableType(varId)
      if tipo != -1:
        return tipo
    return self.functions["_Global"].getVariableType(varId)

  def getFunctionReturnType(self, functionId):
    if self.existsFunction(functionId) == 0:
      return -1
    return self.functions[functionId].retType 

  def getParams(self, functionId):
    if self.existsFunction(functionId) == 0:
      return -1
    return self.functions[functionId].getParams()

  def pprint(self):
    iTam = self.size()
    for func in self.functions:
      self.functions[func].pprint(func)
      iTam = iTam - 1
      if iTam > 0:
        print("\n")

  def __repr__(self):
    return "%s" %(str(self.functions))

  def __str__(self):
    return "%s" %(str(self.functions))
