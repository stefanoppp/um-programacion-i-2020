import os


class LectorDeVentas():
    def __init__(self, archivo):
        self.archivo = archivo
        self.path = __file__.replace("ejercicio17.py", "")
        self.texto = open(self.path + self.archivo).read()

    def readVenta(self, nombre):

        self.line = self.texto[self.texto.find(nombre):]
        self.line = self.line[:self.line.find("\n")]

        return self.line

    def addToJSON(self, nombre):
        self.lista = self.readVenta(nombre).split(", ")

        self.line = ("{nombre:" + self.lista[0] +
                     ", monto: \$" + self.lista[1] +
                     ", descripcion:" + self.lista[2] +
                     ", forma de pago:" + self.lista[3] + "}")

        os.system("echo " +
                  self.line +
                  " >> " +
                  self.path +
                  self.archivo[:self.archivo.find(".")] +
                  ".json")


"""
archivo = "txt.txt"
ejercicio17 = LectorDeVentas(archivo)

nombre = "Once Ka"

ejercicio17.addToJSON(nombre)
"""

# os.system("cat " + ejercicio17.path + "txt.json")
