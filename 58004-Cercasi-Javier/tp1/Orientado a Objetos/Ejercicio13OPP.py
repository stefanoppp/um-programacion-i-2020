'''Generar 10 números aleatorios, mostrarlos por pantalla y mostrar
el promedio.'''
import random


class Promedio():

    def __init__(self):
        self.a = 0

    def generar(self):

        n = []

        for i in range(10):
            n.append(random.randrange(500))
            self.a += n[i]

        prom = self.a/10
        return(n, prom)

    def pantalla(self, n, prom):
        print("\nLos numeros son: ", n)
        print("\nEl promedio de los numeros es : ", prom)


if __name__ == "__main__":
    P = Promedio()
    x, y = P.generar()
    P.pantalla(x, y)
