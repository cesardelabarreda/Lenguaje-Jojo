
from Metodo import Method
from Atributo import Atribute

class Class:
    def __init__(self):
        self.methods = {}
        self.atributes = {}
        self.classes = []

    def emptyMethod(self):
        return self.metodos == {}

    def emptyAtributes(self):
        return self.atributes == {}

    def emptyClasses(self):
        return self.classes == []

    def sizeMethods(self):
        return len(self.methods)

    def sizeMethods(self):
        return len(self.methods)

    def sizeAtributes(self):
        return len(self.atributes)

    def sizeClasses(self):
        return len(self.classes)

    def clear(self):
        self.methods.clear()
        self.atributes.clear()
        self.classes.clear()

    def clearMethodVars(self, methodId):
        self.methods[methodId].clearVars()

    def clearPrivateAtributes(self):
        for atr in self.atributes:
            if atr.atrEncap == 1:
                del self.atributes[atr]

    def existsMethod(self, methodId):
        return methodId in self.methods

    def existsAtribute(self, atributeId):
        return atributeId in self.atributes

    def existsVariable(self, methodId, varId):
        if self.existsMethod(methodId):
            if self.methods[methods].existsVar(varId):
                return 1
        return self.existsAtribute(varId)

    def insertMethod(self, methodId, methodRetType = 0, methodEncap = 0):
        if self.existsMethod(methodId):
            return 0

        meth = Method(methodRetType, methodEncap)
        self.methods[methodId] = meth
        return 1

    def insertVar(self, methodId, varId):
        if self.existsMethod(methodId) == 0:
            return 0
        return self.methods[methodId].insertVar(varId)

    def insertParam(self, methodId, paramType):
        if self.existsMethod(methodId) == 0:
            return 0
        return self.methods[methodId].insertParam(paramType)

    