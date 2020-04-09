'''Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es un número primo o no.'''


class Numero():

    def __init__(self):
        self.num = 0

    def ingreso(self):
        self.num = int(input("Ingrese un numero para detectar si es primo:\n"))
        return(self.num)


class Primo():

    def chequeo(self, numero):

        if numero <= 1:
            print("No es numero primo")

        elif numero > 1:
            for i in range(2, numero):
                if numero % i == 0:         # Si el resto de dividir un n * entre (2, 3, etc) es 0, no es primo.
                    print("No es numero primo")
                    return False

            print("Es numero primo")


if __name__ == "__main__":
    P = Primo()
    N = Numero()
    numero = N.ingreso()
    P.chequeo(numero)
