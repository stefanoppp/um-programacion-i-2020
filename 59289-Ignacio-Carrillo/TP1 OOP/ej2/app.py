from pizza import Pizza
from tipo import Tipo
import os

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        pizza=Pizza()
        pizza.setTipo()
        tipo1=Tipo()
        tipo1.setIngredientes(pizza.getTipo())
        os.system("clear")

        print("\nTipo de pizza:",pizza.getTipo())
        print("Ingredientes: ",end="")
        lista=tipo1.getIngredientes()
        for i in range(len(lista)):
            if i==0:
                print(lista[i],end="")
            else:
                print(",",lista[i],end="")
        print()


if __name__ == '__main__':
    app=App()
    app.ejecutar()
