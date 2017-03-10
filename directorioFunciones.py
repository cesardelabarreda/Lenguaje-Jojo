
from Funcion import Function

class diccionarioFunciones:
    def __init__(self):
        self.functions = {}

    def empty(self):
        return self.functions == {}

    def size(self):
        return len(self.functions)

    def clear(self):
        self.functions.clear()

    def existsFunction(self, functionId):
        return functionId in self.functions

    def insertFunction(self, functionId, functionEncap = None):
        if self.existsFunction(functionId):
            return 0


        if functionEncap == None:
            func = Function()

        else:
            func = Function(functionEncap)

        self.functions[function] = func
        return 1

    def insertVar(self, functionId, varId):
        return self.functions[functionId].insertVar(varId)

    def insertParam(self, functionId, paramType):
        return self.functions[functionId].insertParam(paramType)