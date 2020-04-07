import json


class LectorDeVentas():
    def __init__(self, archivo):
        self.archivo = archivo
        self.path = __file__.replace("ejercicio17.py", "")
        self.texto = open(self.path + self.archivo).read()

    def listToDict(self, lista):
        result = {
                  "nombre": lista[0],
                  "monto": int(lista[1]),
                  "descripcion": lista[2],
                  "forma de pago": lista[3]
                  }
        return result

    def convertToJSON(self):
        self.archivoJSON = self.archivo[:self.archivo.find(".")] + ".json"

        textoLista = self.texto.split("\n")[:-1]
        self.lista = [self.listToDict(item.split(", ")) for item in textoLista]

        self.JSON = open(self.path + self.archivoJSON, "w")
        json.dump(self.lista, self.JSON, indent=4)
        self.JSON.close()


"""
archivo = "txt.txt"
ejercicio17 = LectorDeVentas(archivo)

ejercicio17.convertToJSON()
"""
"""
import os
os.system("cat " + ejercicio17.path + "txt.json")
"""
