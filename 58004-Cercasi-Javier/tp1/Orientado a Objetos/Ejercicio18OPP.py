'''Modificar el programa del ejercicio 17 agregando un control de datos vacíos.
Si por algún motivo alguno de los datos viene vacío o igual a "" debemos
generar una excepción indicando que ocurrió un problema con la fuente de datos
y notificar por pantalla. La excepción debe ser una excepción propia.'''

from Ejercicio17OPP import (Registro, EntradaSalida, Salida)


class EmptyValue(Exception):
    pass


class Vacio():

    def chequeo(self, x, z):
        self.lista = x
        if z:
            if ((len(self.lista[z]) == 0) or (len(self.lista[z+1]) == 0) or
               (len(self.lista[z+2]) == 0) or (len(self.lista[+3]) == 0)):

                print("\nHay un valor vacio\n\n")
                raise EmptyValue()      # Juan es el usuario con datos vacios.


if __name__ == "__main__":
    E = EntradaSalida()
    R = Registro()
    S = Salida()
    V = Vacio()
    x = E.traductor()
    y = E.ingreso()
    z = R.buscador(x, y)
    S.exportar(x, y, z)
    V.chequeo(x, z)
