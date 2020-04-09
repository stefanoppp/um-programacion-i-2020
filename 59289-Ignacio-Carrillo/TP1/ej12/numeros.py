from random import randint

class Numeros():

    def __init__(self):
        self.numero=0
        self.diccionario={}

    def setAleatorios(self):
        repeticiones=randint(0,20)
        for i in range(repeticiones):
            self.numero=randint(1,10)
            self.diccionario.setdefault(str(i),self.numero)

    def getAleatorios(self):
        return self.diccionario

    