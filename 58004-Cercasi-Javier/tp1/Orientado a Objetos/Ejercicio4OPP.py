'''Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo, de altura el
número introducido.'''


class Triangulo:

    def __init__(self):
        self.num = 0

    def ingreso(self):
        self.num = int(input("Ingrese un numero entero positivo:\n"))
        return(self.num)

    def pantalla(self):
        for i in range(self.ingreso()+1):
            print(i*"*")


if __name__ == "__main__":
    T = Triangulo()
    T.pantalla()
