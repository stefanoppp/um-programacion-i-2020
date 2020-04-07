from texto import Texto
import os

class App():

    def __init__(self):
        self.palabras=[]
        self.repeticiones=[]
        self.diccionario={}

    def ejecutar(self):
        texto=Texto()
        texto.setTexto()
        self.analisis(texto.getTexto())
        self.imprimir()

    def analisis(self,texto):
        self.palabras=texto.split()
        for w in self.palabras:
            self.repeticiones.append(self.palabras.count(w))
        self.diccionario=dict(zip(self.palabras,self.repeticiones))

    def imprimir(self):
        os.system("clear clc")
        lista_aux=[]
        for key in self.diccionario:
            lista_aux.append((self.diccionario[key],key))
        lista_aux.sort(reverse=True)
        for i in range(len(lista_aux)):
            if(i==0):
                print("Numero".center(8),"Palabra".center(14),"Repeticiones".center(14),end="\n\n")
            print(str(i+1).center(6),"{}{}".format(lista_aux[i][1].center(17),str(lista_aux[i][0]).center(15)))  
        print()   

if __name__ == "__main__":
    app=App()
    app.ejecutar()