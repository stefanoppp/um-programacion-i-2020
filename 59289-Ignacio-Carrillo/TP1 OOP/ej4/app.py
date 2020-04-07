from numero import Numero

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        numero1=Numero()
        numero1.setNumero()
        print()
        for i in range(numero1.getNumero()):
            print(i+1,"|",end="")
            for j in range(i+1):
                print("*",end="")
            print("")
        print()

if __name__ == '__main__':
    app=App()
    app.ejecutar()