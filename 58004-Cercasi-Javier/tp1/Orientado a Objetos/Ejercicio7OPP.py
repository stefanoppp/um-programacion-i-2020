'''Escribir un programa en el que se pregunte al usuario por una frase y una
letra, y muestre por pantalla el número de veces que aparece la letra en
la frase.'''


class Usuario():

    def __init__(self):
        self.frase = ''
        self.letra = ''

    def ingreso(self):
        self.frase = (input("\nIngrese una frase:\n"))
        self.letra = input("\nIngrese una letra:\n")
        return(self.frase, self.letra)


class Frecuencia():

    def pantalla(self, frase, letra):

        c = 0
        for i in frase:
            if letra == i:
                c += 1
        print("La letra ha aparecido "+str(c)+" vez/veces")


if __name__ == "__main__":
    F = Frecuencia()
    U = Usuario()
    x, y = U.ingreso()
    F.pantalla(x, y)
