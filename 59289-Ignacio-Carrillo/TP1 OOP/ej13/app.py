from numeros import Numeros
import os

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        aleatorios=Numeros()
        aleatorios.setAleatorios()
        self.imprimir(aleatorios.getAleatorios())
    
    def imprimir(self,lista):
        os.system("clear")
        contador=0
        for i in range(len(lista)):
            contador=contador+lista[i]
        contador=contador/len(lista)
        print("\nLos numeros generados son:",lista)
        print("\nEl promedio es:",contador)
        print()

if __name__ == "__main__":
    app=App()
    app.ejecutar()