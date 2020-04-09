'''Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla todos los números impares desde 1 hasta ese
número separados por comas.'''


class Impares():

    def __init__(self):
        self.num = 0

    def ingreso(self):
        self.num = int(input("Ingrese un numero entero positivo:\n"))
        return(self.num)

    def logica(self):
        n = ''
        for i in range(1, self.ingreso(), 2):
            n = n+str(i)+","
        return(n)

    def pantalla(self):
        print("Los numeros impares son: "+self.logica())


if __name__ == "__main__":
    N = Impares()
    N.pantalla()
