import os


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


class Main():

    def __init__(self, archivo):
        self.archivo = archivo
        self.path = __file__.replace("ejercicio19.py", "")

    def createPerson(self, nombre):

        self.texto = open(self.path + self.archivo).read()

        self.texto = self.texto[self.texto.find(nombre):]

        self.lista = self.texto[:self.texto.find("\n")].split(", ")

        persona = Venta(self.lista[4],
                        self.lista[5],
                        self.lista[0],
                        self.lista[1],
                        self.lista[2],
                        self.lista[3])
        return persona

    def addToJSON(self, ventas):

        self.line = ("{nombre:" + ventas.getTarjeta().getNombre() +
                     ", monto: \$" + ventas.getMonto() +
                     ", descripcion:" + ventas.getDescripcion() +
                     "}")

        os.system("echo " +
                  self.line +
                  " >> " +
                  self.path +
                  self.archivo[:self.archivo.find(".")] +
                  ".json")

    def countWords(self):

        self.text = open(self.path + self.archivo).read()

        self.text = self.text.replace("\n", " ")
        self.text = self.text.replace(",", "")
        self.text = self.text.replace(".", "")
        self.text = self.text.replace("(", "")
        self.text = self.text.replace(")", "")
        self.text = self.text.lower()
        self.text = self.text.split(" ")
        [self.text.remove("") for i in range(self.text.count(""))]

        self.text.sort()

        self.dicc = {}
        for item in self.text:
            self.dicc[item] = self.text.count(item)

        print("cantidad de palabras: " + str(len(self.text)))

        print("\n\n\n20 palabras mas repetidas: ")
        for item in sorted(self.dicc, key=self.dicc.get, reverse=True)[:20]:
            print(item + " " + str(self.dicc[item]))

        print("\n\n\nTodas las palabras y sus cantidades: ")
        for item in self.dicc.items():
            print(str(item[0]) + " " + str(item[1]))


"""
example = Main("tt.txt")

persona1 = example.createPerson("Ocho Hache")

persona2 = example.createPerson("Uno A")

example.addToJSON(persona2)

example.addToJSON(persona1)
"""
# example.countWords()
