from io import open
import os
from ej_16 import Venta


class Interfaz():
    def interfaz(self):
        path = os.path.dirname(os.path.abspath(__file__))
        # path toma la ruta absoluta del directorio sobre
        #  el cual el programa reside
        nombre = input("Ingrese el nombre del archivo:\n")
        print("\nLas ventas producidas son:\n\n")
        archivo = open(path + "/" + nombre + ".txt", "r")
        # agregamos el archivo a la ruta del path y abrimos el archivo
        x = Venta(archivo)
        dicc = x.read_line()
        for key in dicc:
            print(key, "\n")
            print(dicc[key], "\n")
        archivo.close()


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
