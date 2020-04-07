class Texto():

    def __init__(self):
        self.lista=[]

    def setTexto(self):
        self.archivo=open("/Users/NachoC/Documents/codigos/Programacion_1/um-programacion-i-2020/59289-Ignacio-Carrillo/TP1 OOP/ej15/venta.txt","r")
        for linea in self.archivo.readlines():
            if linea!="" and linea!="\n":
                linea=linea.replace("\n","")
                self.lista.append(linea.split(", "))

    def getTexto(self):
        return self.lista