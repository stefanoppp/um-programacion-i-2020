class LectorDeVentas():
    def __init__(self, archivo):
        self.archivo = archivo
        self.path = __file__.replace("ejercicio15.py", "")
        self.texto = open(self.path + self.archivo).read()

    def readVenta(self, nombre):

        self.line = self.texto[self.texto.find(nombre):]
        self.line = self.line[:self.line.find("\n")]

        return self.line


"""
archivo = "txt.txt"
ejercicio15 = LectorDeVentas(archivo)

nombre = "Once Ka"
print(
      ejercicio15.readVenta(nombre)
      )
"""
