
from Metodo import Method

class dicClass:
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

    def insertMethod(self, classId, methodId, methodRetType = 0, methodEncap = 0):
        if self.existsClass(classId) == 0:
            return 0
        return self.classes[classId].insertMethod(methodId, methodRetType, methodEncap)

    def insertVar(self, classId, methodId, varId):
        if self.existsClass(classId) == 0:
            return 0
        return self.classes[classId].insertVar(methodId, varId)

    def insertParam(self, classId, methodId, paramType):
        if self.existsClass(classId) == 0:
            return 0
        return self.classes[classId].insertParam(methodId, paramType)

    