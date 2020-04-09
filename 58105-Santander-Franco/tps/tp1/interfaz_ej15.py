from io import open
import os
from ej_15 import Venta


class Interfaz():
    def interfaz(self):
        path = os.path.dirname(os.path.abspath(__file__))
        # path toma la ruta absoluta del directorio sobre
        #  el cual el programa reside
        nombre = input("Ingrese el nombre del archivo:\n")
        print("\nLas ventas producidas son:\n")
        archivo = open(path + "/" + nombre + ".txt", "r")
        # agregamos el archivo a la ruta del path y abrimos el archivo
        x = Venta(archivo)
        x.read_line()
        archivo.close()


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
