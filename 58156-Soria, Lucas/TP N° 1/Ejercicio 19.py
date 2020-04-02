'''
Crear un programa similar al ejercicio 18 (incluyendo la funcionalidad del ejercicio 14) donde
los datos del archivo de texto serán:
Nombre y apellido, número de tarjeta de crédito, código de verificación, tipo de tajeta de
crédito, monto de la venta, descripción de venta.
Los datos debén manejarse de la siguiente manera:
Crear una clase TarjetaCredito que almacene los datos de: Nombre y apellido, número de
tarjeta de crédito, código de verificación, tipo de tajeta de crédito.
Crear una clase Venta que almacene los datos de: monto de la venta, descripción de venta y
un objeto de la clase TarjetaCredito.
El formato de los datos JSON deberá respetar el formato de Venta con los datos de monto y
descripción y el objeto de la clase Venta.
'''

class ErrorValorNoValido(Exception):
    print("Ocurrió un problema con la fuente de datos")


class TejetaCredito():

    def __init__(self):
        pass

    def AlmacenaTarjeta(self, nom, nro, cod, tipo):
        pass


class Venta():

    def __init__(self):
        pass
    
    def AlmacenaVenta(self, monto, desc, tar):
        pass



archivo = open("/home/lucas/1 Prog I/um-programacion-i-2020/58156-Soria, Lucas/TP N° 1/Ventas.txt", "r")
archivo1 = open("/home/lucas/1 Prog I/um-programacion-i-2020/58156-Soria, Lucas/TP N° 1/Ventas.json", "a")
texto = '[\n'
archivo1.write(texto)
c = 0
for line in archivo.readlines():
    try:
        linea = line.replace("\n", "").replace(", ", "|||").split("|||")
        if c == 1:
            texto = ',\n\t{\n\t\t"nombre": "' + linea[0] + '",\n\t\t"monto": ' + str(round(float(linea[1]), 2)) + ',\n\t\t"descripcion": "' + linea[2] +'",\n\t\t"formapago": "' + linea[3] + '"\n\t}'
        else:
            texto = '\t{\n\t\t"nombre": "' + linea[0] + '",\n\t\t"monto": ' + str(round(float(linea[1]), 2)) + ',\n\t\t"descripcion": "' + linea[2] +'",\n\t\t"formapago": "' + linea[3] + '"\n\t}'
            c += 1
    except ErrorValorNoValido:
        pass
    archivo1.write(texto)
archivo1.write('\n]\n')
archivo.close()
archivo1.close()
