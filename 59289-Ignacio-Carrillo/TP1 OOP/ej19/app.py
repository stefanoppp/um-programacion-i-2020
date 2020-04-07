from texto import Texto
import os
import json
from excepcion import miError
from venta import Venta

class App():

    def __init__(self):
        self.lista_de_diccionarios=[]
        self.lista_etiqueta=["Nombre","Numero de Tarjeta","Codigo de verificacion","Tipo de tarjeta","Monto","Descripcion"]

    def ejecutar(self):
        texto=Texto()
        texto.setTexto()
        self.convertir(texto.getTexto())
        self.archivar()
 
    def convertir(self,lista):
        for i in range(len(lista)):
            self.lista_de_diccionarios.append({})
            obj=Venta(lista[i])
            obj.setValores()
            flag=0
            for j in range(len(self.lista_etiqueta)):
                if(obj.getValores()[j]==""):
                    flag=1
                self.lista_de_diccionarios[i].setdefault(self.lista_etiqueta[j],obj.getValores()[j])

            try:    
                if (flag==1):
                    raise miError
                else:
                    self.imprimir(i)
                
            except miError:
                print("**ERROR** Ocurrio un problema con la fuente de datos de la venta {}\n".format(i+1))

    def imprimir(self,i):
        print(self.lista_de_diccionarios[i],end="\n\n")
    
    def archivar(self):
        with open('/Users/NachoC/Documents/codigos/Programacion_1/um-programacion-i-2020/59289-Ignacio-Carrillo/TP1 OOP/ej19/ARCHIVO_ORIGINAL.json','w') as file:
            json.dump(self.lista_de_diccionarios, file, indent=4)

if __name__ == "__main__":
    os.system("clear clc")
    app=App()
    app.ejecutar()