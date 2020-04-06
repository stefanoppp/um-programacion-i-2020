archivo = input("ingrese el nombre del archivo  ")
path = __file__.replace("ejercicio16.py", "")

texto = open(path + archivo).read()

nombre = input("ingrese el nombre del vendedor  ")

texto = texto[texto.find(nombre):]

lista = texto[:texto.find("\n")].split(", ")

print("nombre:", lista[0], ", monto: $", lista[1], ", descripcion:", lista[2], ", forma de pago:", lista[3])
