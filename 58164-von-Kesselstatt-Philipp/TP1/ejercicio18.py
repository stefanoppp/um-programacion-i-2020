import os


class EmptyValue(Exception):
    pass


def ejercicio18(archivo, nombre):

    path = __file__.replace("ejercicio18.py", "")

    texto = open(path + archivo).read()

    texto = texto[texto.find(nombre):]

    lista = texto[:texto.find("\n")].split(", ")

    if "" in lista:
        raise EmptyValue()

    line = ("{nombre:" + str(lista[0]) +
            ", monto: \$" + str(lista[1]) +
            ", descripcion:" + str(lista[2]) +
            ", forma de pago:" + str(lista[3]) + "}")

    os.system("echo " +
              line +
              " >> " +
              __file__.replace("ejercicio18.py", "") +
              archivo[:archivo.find(".")] +
              ".json")


"""
archivo = input("ingrese el nombre del archivo  ")
nombre = input("ingrese el nombre del vendedor  ")

ejercicio18(archivo, nombre)
"""

ejercicio18("txt.txt", "Dato Vacio")
