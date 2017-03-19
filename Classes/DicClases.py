
from Clase import Class

class DicClass:
    def __init__(self):
        self.classes = {}

    def empty(self):
        return self.classes == {}

    def size(self):
        return len(self.classes)

    def clear(self):
        self.classes.clear()

    def existsClass(self, classId):
        return classId in self.classes

    def existsAtribute(self, classId, atributeId):
        if self.existsClass(classId) == 0:
            return 0

        if self.classes[classId].existsAtribute(atributeId):
            return 1
       
        for clas in self.classes[classId]:
            if self.existsAtribute(clas, atributeId) == 1:
                return 1
        return 0

    def existsVariable(self, classId, methodId, varId):
        if self.existsClass(classId) == 0:
            return 0

        if self.classes[classId].existsVariable(methodId, varId):
            return 1
        return self.existsAtribute(classId, atributeId)

    def getAtributeType(self, classId, atributeId):
        if self.existsClass(classId) == 0:
            return 0

        if self.classes[classId].existsAtribute(atributeId):
            return self.classes[classId].getAtributeType(atributeId)
       
        for clas in self.classes[classId]:
            if self.existsAtribute(clas, atributeId) == 1:
                return 1
        return 0


    def getVariableType(self, classId, methodId, varId):
        if self.existsClass(classId) == 0:
            return -1

        if self.classes[classId].existsMethodVariable(methodId, varId):
            return self.classes[classId].getVarType(methodId, varId)
        return self.getAtributeType(classId, varId)


    def insertHamon(self, classId, classHamon):
        if self.existsClass(classId) == 0:
            return 0
        if self.existsClass(classHamon) == 0:
            return 0
        return self.classes[classId].insertHamon(classHamon)

    def insertClass(self, classId):
        if self.existsClass(classId):
            return 0

        clas = Class()
        self.classes[classId] = clas

    def insertMethod(self, classId, methodId, methodRetType, methodEncap):
        if self.existsClass(classId) == 0:
            return 0
        return self.classes[classId].insertMethod(methodId, methodRetType, methodEncap)

    def insertVar(self, classId, methodId, varId, varType):
        if self.existsClass(classId) == 0:
            return 0
        return self.classes[classId].insertVar(methodId, varId, varType)

    def insertParam(self, classId, methodId, varId, paramType):
        if self.existsClass(classId) == 0:
            return 0
        return self.classes[classId].insertParam(methodId, varId, paramType)

    def insertAtribute(self, classId, atrId, atrType, atrEncap):
        if self.existsClass(classId) == 0:
            return 0
        return self.classes[classId].insertAtribute(atrId, atrType, atrEncap)
    
    def __repr__(self):
        return "%s" %(str(self.classes))

    def __str__(self):
        return "%s" %(str(self.classes))