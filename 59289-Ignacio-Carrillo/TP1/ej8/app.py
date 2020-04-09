import os
from asignatura import Asignatura

class App():

    def __init__(self):      
        self.lista_materia=["Matematica","Fisica","Quimica","Historia","Lengua"]
        self.lista_obj=[]

    def ejecutar (self):
        for i in range(len(self.lista_materia)):
            obj=Asignatura(self.lista_materia[i])
            self.lista_obj.append(obj)
            self.lista_obj[i].setNota(self.lista_obj[i].getNombre())

        os.system("clear clc")
        for i in range(len(self.lista_materia)):
            self.imprimir(self.lista_obj[i].getNombre(),self.lista_obj[i].getNota())
        print()

    def imprimir (self,materia,nota):
        print("\nEn {} has sacado {}".format(materia,nota))


if __name__ == "__main__":
    app=App()
    app.ejecutar()