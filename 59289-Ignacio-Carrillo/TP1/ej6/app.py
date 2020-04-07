from numero import Numero

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        numero1=Numero()
        numero1.setNumero()
        if numero1.es_primo(numero1.getNumero()):
            print("\nEl numero",numero1.getNumero(),"es un numero primo")
        else:
            print("\nEl numero", numero1.getNumero(), "NO es un numero primo")

if __name__ == '__main__':
    app=App()
    app.ejecutar()