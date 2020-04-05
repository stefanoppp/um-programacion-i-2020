class EmptyValue(Exception):
    pass


class LectorDeVentas():
    def __init__(self, archivo):
        self.archivo = archivo
        self.path = __file__.replace("ejercicio18.py", "")
        self.texto = open(self.path + self.archivo).read()

    def convertToJSON(self):
        self.lista = [item.split(", ") for item in self.texto.split("\n")[:-1]]
        self.archivoComoJSON = '{"ventas": [\n'

        for item in self.lista:

            if "" in item:
                raise EmptyValue()

            self.archivoComoJSON += ('{"nombre": "' + item[0] +
                                     '", "monto": ' + item[1] +
                                     ', "descripcion": "' + item[2] +
                                     '", "forma de pago": "' + item[3] +
                                     '"},\n')





        self.archivoComoJSON = self.archivoComoJSON[:-2]
        self.archivoComoJSON += '\n]}\n'

        self.JSON = open(self.path +
                         self.archivo[:self.archivo.find(".")] +
                         ".json", "w")
        self.JSON.write(self.archivoComoJSON)

        self.JSON.close()


"""
archivo = "txt.txt"
ejercicio18 = LectorDeVentas(archivo)

ejercicio18.convertToJSON()
"""

# os.system("cat " + ejercicio18.path + "txt.json")
