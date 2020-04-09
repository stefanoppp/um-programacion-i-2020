'''Crear un programa que lea el archivo del ejercicio 15 y lo convierta
a formato JSON con el siguiente formato: {"nombre":"xxxxxxxxx",'
'monto":xxxx.xx, "descripcion":"xxxxxxxx", "formapago":"xxxx"}
Debemos mostrarlo por pantalla y crear un archivo llamado ARCHIVO_ORIGINAL.json
donde guardaremos los objetos JSON convertidos
El nombre ARCHIVO_ORIGINAL debe ser el que se definió para el archivo de
datos.'''

import json

from Ejercicio15OPP import EntradaSalida
from Ejercicio16OPP import Registro


class Salida():

    def exportar(self, x, y, z):
        self.lista = x
        self.nombre = y

        if z:

            Ejercicio17 = ("{nombre:" + str((len(self.lista[z]))*"x") +
                           ", monto: " + str(((len(self.lista[z+1]))-1)*"x") +
                           ", descripcion:" + str(((len(self.lista[z+2]))-1)*"x") +
                           ", forma de pago:" + str(((len(self.lista[z+3]))-1)*"x")+"}")

            with open('Ejercicio17.json', 'w') as file:
                json.dump(Ejercicio17, file, indent=4)


if __name__ == "__main__":
    E = EntradaSalida()
    R = Registro()
    S = Salida()
    x = E.traductor()
    y = E.ingreso()
    z = R.buscador(x, y)
    S.exportar(x, y, z)
