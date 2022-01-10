class animal(object):
    def __init__(self):
        self.age = 0 
        self.name = ''
    def addName(self,name):
        self.name = name
    def increament(self):
        self.age += 1
kida1 = animal()
kida1.type = 'elephant'
kida1.addName('gajju')
print(kida1.age)
kida1.increament()
print(kida1.age)
print(kida1.type)
