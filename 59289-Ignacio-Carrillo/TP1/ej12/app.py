from numeros import Numeros
import os

class App():

    def __init__(self):
        pass
    
    def ejecutar(self):
        aleatorios=Numeros()
        aleatorios.setAleatorios()
        self.imprimir(aleatorios.getAleatorios())

    def imprimir(self,diccionario):
        valores=diccionario.values()
        valores=list(valores)
        valores.sort(reverse=True)
        print("\nResultado:",valores)
        print()

if __name__ == "__main__":
    os.system("clear")
    app=App()
    app.ejecutar()
