import os
import json


class EmptyValue(Exception):
    pass


class TarjetaCredito():
    def __init__(self,
                 nombre_y_apellido=None,
                 numero_de_tarjeta_de_credito=None,
                 codigo_de_verificacion=None,
                 tipo_de_tajeta_de_credito=None):

        self.nombre = nombre_y_apellido
        self.nro = numero_de_tarjeta_de_credito
        self.ver = codigo_de_verificacion
        self.tipo = tipo_de_tajeta_de_credito

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre_y_apellido):
        self.nombre = nombre_y_apellido

    def getNumero(self):
        return self.nro

    def setNumero(self, numero_de_tarjeta_de_credito):
        self.nro = numero_de_tarjeta_de_credito

    def getVerificacion(self):
        return self.ver

    def setVerificacion(self, codigo_de_verificacion):
        self.ver = codigo_de_verificacion

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo_de_tajeta_de_credito):
        self.tipo = tipo_de_tajeta_de_credito

    def __repr__(self):
        return {
                 "Nombre y apellido": self.nombre,
                 "número de tarjeta de credito": self.nro,
                 "código de verificación": self.ver,
                 "tipo de tajeta de crédito": self.tipo,
                }


class Venta():
    def __init__(self,
                 monto_de_la_venta=None,
                 descripcion_de_la_venta=None,
                 nombre_y_apellido=None,
                 numero_de_tarjeta_de_credito=None,
                 codigo_de_verificacion=None,
                 tipo_de_tajeta_de_credito=None):

        self.monto = monto_de_la_venta
        self.descripcion = descripcion_de_la_venta
        self.tarjeta = TarjetaCredito(
                                      nombre_y_apellido,
                                      numero_de_tarjeta_de_credito,
                                      codigo_de_verificacion,
                                      tipo_de_tajeta_de_credito
                                      )

    def getMonto(self):
        return self.monto

    def setMonto(self, monto_de_la_venta):
        self.monto = monto_de_la_venta

    def getDescripcion(self):
        return self.descripcion

    def setVerificacion(self, descripcion_de_la_venta):
        self.ver = descripcion_de_la_venta

    def getTarjeta(self):
        return self.tarjeta

    def setTarjeta(self, tajeta_de_credito):
        self.tarjeta = tajeta_de_credito

    def __repr__(self):
        return {
            "Nombre y apellido": self.getTarjeta().getNombre(),
            "monto": self.monto,
            "descripcion": self.descripcion
        }


class Ejercicio19():

    def __init__(self, archivo):
        self.archivo = archivo
        self.path = __file__.replace("ejercicio19.py", "")
        self.archivoJSON = self.archivo[:self.archivo.find(".")] + ".json"
        self.texto = open(self.path + self.archivo).read()
        self.lista = []

        for item in self.texto.split("\n")[:-1]:

            if "" in item.split(", "):
                raise EmptyValue()

            self.lista.append(item.split(", "))

        self.listOfPeople = [self.createPerson(item)
                             for item in self.lista]

    def createPerson(self, lista):

        persona = Venta(lista[4],
                        lista[5],
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3])
        return persona

    def convertToJSON(self):

        self.listOfDicts = [item.__repr__() for item in self.listOfPeople]

        self.JSON = open(self.path + self.archivoJSON, "w")
        json.dump(self.listOfDicts, self.JSON, indent=4)
        self.JSON.close()

    def readFile(self):

        os.system("cat " +
                  self.path +
                  self.archivoJSON)

    def getPeople(self):
        return self.listOfPeople


"""
example = Ejercicio19("tt.txt")

example.convertToJSON()
"""
# example.readFile()

# print(example.getPeople()[4].getTarjeta().getNumero())
