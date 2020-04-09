from random import randint

class Ejercicio():

    def __init__(self):

        self.diccionario = {}

        for i in range(10):
    
            numero = randint(0,10)

            self.diccionario[i] = numero

    def mostrar(self):

        lista = list(self.diccionario.values())

        lista.sort()

        print (lista)

def main():

    ejercicio = Ejercicio()
    ejercicio.mostrar()

if __name__ == "__main__":
    main()








