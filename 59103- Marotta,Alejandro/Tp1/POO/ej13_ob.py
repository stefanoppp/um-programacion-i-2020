from random import randint

class Promedio():

    def __init__(self):

        self.promedio = 0

    def generar(self):

        for i in range(10):    
   
            numero = randint(0,10)

            print(numero)

            self.promedio = self.promedio + numero

    def mostar(self):

        print("El promedio es: ",self.promedio/10)


def main():

    numero = Promedio()

    numero.generar()
    numero.mostar()

if __name__ == "__main__":
    main()









