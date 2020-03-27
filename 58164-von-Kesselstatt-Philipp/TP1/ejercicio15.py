archivo = input("ingrese el nombre del archivo  ")
path = __file__.replace("ejercicio15.py", "")

texto = open(path + archivo).read()

nombre = input("ingrese el nombre del vendedor  ")

texto = texto[texto.find(nombre):]

print(texto[:texto.find("\n")])
