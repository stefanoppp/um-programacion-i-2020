import math

class Numero():

    def __init__(self):
        self.numero=0

    def setNumero(self):
        while True:
            try:
                self.numero=int(input("\nIngrese un entero mayor a cero: "))
                if self.numero<=0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nEl numero ingresado es invalido. Intente nuevamente")

    def getNumero(self):
        return self.numero

    def es_primo(self,numero):
        if (numero <= 1):
            return False

        for i in range(2, math.ceil(math.sqrt(numero)) + 1):
            if (numero % i == 0 and i != numero):
                return False
        return True
