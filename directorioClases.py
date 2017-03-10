 

 class diccionarioClases:
 	def __init__(self):
        self.list = {}
        self.

    def createClass(self, clase):
    	self.

    def empty(self):
        return self.list == {}

    def size(self):
        return len(self.list)
    
    def insert(self, key, value):
        self.list[key] = value

    def at(self, key):
        return self.list.get(key)

    def erase(self, key):
        del self.list[key]

    def find(self, key):
        return key in self.list

    def clear(self):
        self.list.clear()

# ******************** Codigo para probar el Diccionario ********************
d = Dictionary()                # Crea el diccionario
print(d.empty())                # Muestra True
d.insert("hola", 15)            # {"hola": 15}
d.insert("mundo", 20)           # {"hola": 15, "mundo": 20}
d.insert(12, True)              # {"hola": 15, "mundo": 20, 12: True}
print(d.size())                 # Muestra 3
print(d.at("mufndo"))           # Muestra None
d.insert(False, False)          # {"hola": 15, "mundo": 20, 12: True, False: True}
print(d.find("mundo"))          # Muestra True
print(d.find(True))             # Muestra False
d.erase("mundo")                # {"hola": 15, 12: True, False: True}
print(d.find("mundo"))          # Muestra False
print(d.size())                 # Muestra 3
d.clear()                       # {}
print(d.size())                 # Muestra 0
print(d.empty())                # Muestra True