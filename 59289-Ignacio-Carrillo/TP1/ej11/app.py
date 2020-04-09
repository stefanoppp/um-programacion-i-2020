import os
from materias import Materias

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        materia=Materias()
        materia.setCreditos()
        materias=materia.getCreditos()
        self.imprimir(materias)
    
    def imprimir(self,materia):
        total=0
        for key in materia:
            print (key,"tiene",materia[key],"creditos")
            total=total+materia[key]
        print("\nNumero total de creditos del curso:",total)
        print()

if __name__ == "__main__":
    os.system("clear")
    app=App()
    app.ejecutar()
