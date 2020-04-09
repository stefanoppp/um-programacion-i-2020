'''Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''
from Ejercicio4OPP import Triangulo


class TrianguloR():

    def display(self, num):
        n = ''
        for i in range(num):
            n = " "+str((i+1)*2-1) + n
            print(n)


if __name__ == "__main__":
    T = Triangulo()
    R = TrianguloR()
    x = T.ingreso()
    R.display(x)
