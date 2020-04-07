from random import randint

class Numeros():

    def __init__(self):
        self.numero=0
        self.lista=[]

    def setAleatorios(self):
        repeticiones=10
        for i in range(repeticiones):
            self.numero=randint(0,100)
            self.lista.append(self.numero)

    def getAleatorios(self):
        return self.lista
