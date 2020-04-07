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
        print("")
        for i in range(len(lista)):
            if(i==0):
                print("Venta".center(8),"Nombre".center(18),"Monto".center(18),"Descripcion".center(18),"Forma de pago".center(18),end="\n\n")
            for j in range(len(lista[i])):
                if(j==0):
                    print(str(i+1).center(8),end="")
                print(lista[i][j].center(19),end="")
            print("\n\n")
                

if __name__ == "__main__":
    app=App()
    app.ejecutar()