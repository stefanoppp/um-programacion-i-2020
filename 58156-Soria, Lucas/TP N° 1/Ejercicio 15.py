archivo = open("/home/lucas/1 Prog I/um-programacion-i-2020/58156-Soria, Lucas/Ventas.txt", "r")
print("\nEl archivo contiene la siguiente informacion:\n\n\n")
for line in archivo.readlines():
    print(line)
archivo.close()
