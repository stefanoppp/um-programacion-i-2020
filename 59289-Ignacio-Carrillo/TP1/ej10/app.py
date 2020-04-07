from fecha import Fecha
import os

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        obj=Fecha()
        obj.setFecha()
        diccionario=self.setDiccionario()
        self.imprimir(obj,diccionario)

    def setDiccionario(self):
        diccionario={}
        diccionario['01']='Enero'
        diccionario['02']='Febrero'
        diccionario['03']='Marzo'
        diccionario['04']='Abril'
        diccionario['05']='Mayo'
        diccionario['06']='Junio'
        diccionario['07']='Julio'
        diccionario['08']='Agosto'
        diccionario['09']='Septiembre'
        diccionario['10']='Octubre'
        diccionario['11']='Noviembre'
        diccionario['12']='Diciembre'
        return diccionario

    def imprimir(self,obj,diccionario):
        os.system("clear")
        dia,mes,año=obj.getFecha()
        mes=diccionario[mes]
        print("\n{} de {} de {}".format(dia,mes,año))
        print()

if __name__ == "__main__":
    os.system("clear")
    app=App()
    app.ejecutar()