'''Crear un programa similar al ejercicio 18 (incluyendo la funcionalidad
del ejercicio 14) donde los datos del archivo de texto serán: Nombre y
apellido, número de tarjeta de crédito, código de verificación, tipo de
tajeta de crédito, monto de la venta, descripción de venta. Los datos debén
manejarse de la siguiente manera:

Crear una clase TarjetaCredito que almacene los datos de: Nombre y apellido,
número de tarjeta de crédito, código de verificación, tipo de tajeta de crédito

Crear una clase Venta que almacene los datos de: monto de la venta, descripción
de venta y un objeto de la clase TarjetaCredito.

El formato de los datos JSON deberá respetar el formato de Venta con los datos
de monto y descripción y el objeto de la clase Venta.'''
import json
import sys


class EntradaSalida():

    def __init__(self):

        self.ls = []
        self.nombre = ''
        self.texto = ''
        self.item = []
        self.datos = open("/home/javi/Programacion_1/um-programacion-i-" +
                          "2020/58004-Cercasi-Javier/tp1/Ejercicio19.txt", "r")

    def ingreso(self):
        self.res = input("Ingrese el nombre y apellido para obtener sus " +
                         "datos:\n").title()
        return(self.res)

    def traductor(self):

        self.texto = self.datos.read().replace("\n", ",")
        self.ls = list(self.texto.strip().split(","))
        ubi = 0

        try:
            ubi = self.ls.index(self.ingreso())
            programa = TarjetaCredito(self.ls[ubi], self.ls[ubi+1],
                                      self.ls[ubi+2], self.ls[ubi+3])

            programa1 = Venta(self.ls[ubi+4], self.ls[ubi+5], self.ls[ubi+3])
            return(programa, programa1, ubi)


        except:
            print("\n\nEl nombre es incorrecto\n\n")
            pass
            sys.exit()

    def pantalla(self, programa, programa1):

        print("\nBuen dia estimado cliente.\n\nSus datos son:\n")

        self.item = [" Nombre y apellido:", "Numero de tarjeta de credito:",
                     "Codigo de verificacion:", "Tipo tajeta de credito:",
                     "Monto de la venta:", "Descripcion de venta:"]

        print(self.item[0], programa.get_nombre(), "\n",
              self.item[1], programa.get_tarjeta(), "\n",
              self.item[2], programa.get_codigo(), "\n",
              self.item[3], programa.get_tipo(), "\n",
              self.item[4], programa1.get_monto(), "\n",
              self.item[5], programa1.get_descripcion(), "\n",)

    def exportar(self, programa, programa1, ubi):

        if ubi:
            Ejercicio19 = ("{"+self.item[0]+programa.get_nombre()+", " +
                           self.item[1]+programa.get_tarjeta()+", " +
                           self.item[2]+programa.get_codigo()+", " +
                           self.item[3]+programa1.get_objeto_tajeta()+", " +
                           self.item[4]+programa1.get_monto()+", " +
                           self.item[5]+programa1.get_descripcion() + "}")

            with open('Ejercicio19.json', 'w') as file:
                json.dump(Ejercicio19, file, indent=4)


class TarjetaCredito():
    def __init__(self, nombre, tarjeta, codigo, tipo):
        self.nombre = nombre
        self.tarjeta = tarjeta
        self.codigo = codigo
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_tarjeta(self, tarjeta):
        self.tarjeta = tarjeta

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_nombre(self):
        return self.nombre

    def get_tarjeta(self):
        return self.tarjeta

    def get_codigo(self):
        return self.codigo

    def get_tipo(self):
        return self.tipo


class Venta():
    def __init__(self, monto, descripcion, tipo):
        self.monto = monto
        self.descripcion = descripcion
        self.tipo = tipo

    def set_monto(self, monto):
        self.monto = monto

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_monto(self):
        return self.monto

    def get_descripcion(self):
        return self.descripcion

    def set_objeto_tajeta(self, tipo):
        self.tipo = tipo

    def get_objeto_tajeta(self):
        return self.tipo


if __name__ == "__main__":
    E = EntradaSalida()
    x, y, z = E.traductor()
    E.pantalla(x, y)
    E.exportar(x, y, z)

# def __init__(self, iterable):
# self.listta_de_items = []
# self.__actualizar(iterable)
