from texto import Texto
import os
import json

class App():

    def __init__(self):
        self.lista_de_diccionarios=[]
        self.lista_etiqueta=["Nombre","Monto","Descripcion","Forma de Pago"]

    def ejecutar(self):
        texto=Texto()
        texto.setTexto()
        self.convertir(texto.getTexto())
        self.imprimir()
        self.archivar()
 
    def convertir(self,lista):
        for i in range(len(lista)):
            self.lista_de_diccionarios.append({})
            for j in range(len(lista[i])):
                self.lista_de_diccionarios[i].setdefault(self.lista_etiqueta[j],lista[i][j])

    def imprimir(self):
        os.system("clear clc")
        print()
        for i in range(len(self.lista_de_diccionarios)):
            print(self.lista_de_diccionarios[i],end="\n\n")
        print()
    
    def archivar(self):
        with open('/Users/NachoC/Documents/codigos/Programacion_1/um-programacion-i-2020/59289-Ignacio-Carrillo/TP1 OOP/ej17/ARCHIVO_ORIGINAL.json','w') as file:
            json.dump(self.lista_de_diccionarios, file, indent=4)

if __name__ == "__main__":
    app=App()
    app.ejecutar()