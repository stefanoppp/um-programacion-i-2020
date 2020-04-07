
class Frase():

    def __init__(self):
        self.frase=""
        self.letra='a'

    def setFrase(self):
        self.frase=input("\nIngrese una frase: ")

    def getFrase(self):
        return self.frase

    def setLetra(self):
        while True:
            try:
                self.letra=input(("\nIngrese la letra a estudiar: "))
                self.letra=self.letra.upper() #paso el caracter a mayusc para facilitar condicional
                if (len(self.letra)==1 and ord(self.letra)>64 and ord(self.letra)<91):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\nLa letra ingresada es incorrecta. Intente nuevamente")

    def getLetra(self):
        return self.letra