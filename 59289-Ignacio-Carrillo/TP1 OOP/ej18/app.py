from texto import Texto
import os
import json
from excepcion import miError
class App():

    def __init__(self):
        self.lista_de_diccionarios=[]
        self.lista_etiqueta=["Nombre","Monto","Descripcion","Forma de Pago"]

    def ejecutar(self):
        texto=Texto()
        texto.setTexto()
        self.convertir(texto.getTexto())
        #self.archivar()
 
    def convertir(self,lista):
        for i in range(len(lista)):
            flag=0
            self.lista_de_diccionarios.append({})
            for j in range(len(lista[i])):
                self.lista_de_diccionarios[i].setdefault(self.lista_etiqueta[j],lista[i][j])
                if lista[i][j]=="":
                    flag=1
        
            try:
                if(flag==1):
                    raise miError
                else:
                    self.imprimir(i)
            except miError:
                print("**ERROR** Ocurrio un problema con la fuente de datos de la venta {}\n".format(i+1))

    def imprimir(self,i):
        print(self.lista_de_diccionarios[i],end="\n\n")
    
    def archivar(self):
        with open('/Users/NachoC/Documents/codigos/Programacion_1/um-programacion-i-2020/59289-Ignacio-Carrillo/TP1 OOP/ej18/ARCHIVO_ORIGINAL.json','w') as file:
            json.dump(self.lista_de_diccionarios, file, indent=4)

if __name__ == "__main__":
    os.system("clear clc")
    app=App()
    app.ejecutar()