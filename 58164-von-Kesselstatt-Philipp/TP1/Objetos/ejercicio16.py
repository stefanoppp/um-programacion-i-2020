class LectorDeVentas():
    def __init__(self, archivo):
        self.archivo = archivo
        self.path = __file__.replace("ejercicio16.py", "")
        self.texto = open(self.path + self.archivo).read()

    def readVenta(self, nombre):

        self.line = self.texto[self.texto.find(nombre):]
        self.line = self.line[:self.line.find("\n")].split(", ")

        return (
                "nombre: " + self.line[0] +
                ", monto: $" + self.line[1] +
                ", descripcion: " + self.line[2] +
                ", forma de pago: " + self.line[3]
                )


"""
archivo = "txt.txt"
ejercicio16 = LectorDeVentas(archivo)

nombre = "Once Ka"
print(
      ejercicio16.readVenta(nombre)
      )
"""
