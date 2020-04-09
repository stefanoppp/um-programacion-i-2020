from frase import Frase
import os

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        frase=Frase()
        frase.setFrase()
        frase.setLetra()
        os.system("clear clc")
        reps=app.determinar_veces(frase.getFrase().upper(),frase.getLetra())
        print("\nLa frase ingresada es: ",frase.getFrase().upper())
        print("\nLa letra ingresada es:",frase.getLetra(),", y se repite",reps,"veces")
        print("\n")

    def determinar_veces(self,frase,letra):
        contador=0
        for i in range(len(frase)):
            if(frase[i]==letra):
                contador+=1
        return contador

if __name__ == '__main__':
    app=App()
    app.ejecutar()

