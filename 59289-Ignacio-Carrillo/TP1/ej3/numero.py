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

    def calcular(self,limite):
        self.impares = []
        for i in range(0, limite + 1):
            if (i % 2 != 0):
                self.impares.append(i)
        return self.impares
