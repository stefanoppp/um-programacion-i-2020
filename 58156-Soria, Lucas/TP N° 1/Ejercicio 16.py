archivo = open("/home/lucas/1 Prog I/um-programacion-i-2020/58156-Soria, Lucas/Ventas.txt", "r")
print("\nEl archivo contiene la siguiente informacion:\n\n")
for line in archivo.readlines():
    linea = line.split(",")
    print("Nombre: {}, monto: {}, descripcion: {}, forma de pago: {}".format(linea[0], linea[1], linea[2], linea[3]))
archivo.close()
