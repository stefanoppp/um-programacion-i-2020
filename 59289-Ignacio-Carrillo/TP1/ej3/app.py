from numero import Numero

class App():

    def __init__(self):
        self.impares=[]
        pass

    def ejecutar(self):
        numero=Numero()
        numero.setNumero()
        self.impares=numero.calcular(numero.getNumero())
        print("\nLos numeros impares hasta el numero",numero.getNumero(),"son: ", end="")
        for i in range(len(self.impares)):
            if i==0:
                print("",self.impares[i],end="")
            else:
                print(",",self.impares[i],end="")
        print()
if __name__ == '__main__':
    app=App()
    app.ejecutar()