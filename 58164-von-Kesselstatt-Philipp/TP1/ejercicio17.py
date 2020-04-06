import os

archivo = input("ingrese el nombre del archivo  ")
path = __file__.replace("ejercicio17.py", "")

texto = open(path + archivo).read()

nombre = input("ingrese el nombre del vendedor  ")

texto = texto[texto.find(nombre):]

lista = texto[:texto.find("\n")].split(", ")

line = ("{nombre:" + str(lista[0]) +
        ", monto: \$" + str(lista[1]) +
        ", descripcion:" + str(lista[2]) +
        ", forma de pago:" + str(lista[3]) + "}")

os.system("echo " +
          line +
          " >> " +
          path +
          archivo[:archivo.find(".")] +
          ".json")
