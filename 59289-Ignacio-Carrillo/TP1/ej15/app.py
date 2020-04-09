from texto import Texto
import os

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        texto=Texto()
        texto.setTexto()
        self.imprimir(texto.getTexto())
    
    def imprimir(self,lista):
        os.system("clear clc")
        print("VENTAS: ",end="\n\n")
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if(j==0):
                    print(i+1,end="")
                print(",",lista[i][j],end="")
            print()
        print()
                

if __name__ == "__main__":
    app=App()
    app.ejecutar()