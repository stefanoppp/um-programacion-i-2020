archivo = open("/home/lucas/1 Prog I/um-programacion-i-2020/58156-Soria, Lucas/Ventas.txt", "r")
archivo1 = open("/home/lucas/1 Prog I/um-programacion-i-2020/58156-Soria, Lucas/Ventas.json", "a")
texto = '[\n'
archivo1.write(texto)
c = 0
for line in archivo.readlines():
    linea = line.replace("\n", "").replace(", ", "|||").split("|||")
    if c == 1:
        texto = ',\n\t{\n\t\t"nombre": "' + linea[0] + '",\n\t\t"monto": ' + str(round(float(linea[1]), 2)) + ',\n\t\t"descripcion": "' + linea[2] +'",\n\t\t"formapago": "' + linea[3] + '"\n\t}'
    else:
        texto = '\t{\n\t\t"nombre": "' + linea[0] + '",\n\t\t"monto": ' + str(round(float(linea[1]), 2)) + ',\n\t\t"descripcion": "' + linea[2] +'",\n\t\t"formapago": "' + linea[3] + '"\n\t}'
        c += 1
    archivo1.write(texto)
archivo1.write('\n]')
archivo.close()
archivo1.close()
