"""Modificar el ejercicio 15 y hacer que los datos se muestren con una
etiqueta por delante, algo así como: Nombre: xxxxxxxxx, monto: xxxx.xx,
descripción: xxxxxxxxxx, forma de pago: xxxxxxxx."""

from Ejercicio15OPP import EntradaSalida


class Registro():

    def buscador(self, x, y):
        self.lista = x
        self.nombre = y

        try:
            ubi = self.lista.index(self.nombre)
            print("\nSus datos son:\nNombre:", str((len(self.lista[ubi]))*"x"),
                  "\nMonto de venta:", str(((len(self.lista[ubi+1]))-1)*"x"),
                  "\nDescripcion:", str(((len(self.lista[ubi+2]))-1)*"x"),
                  "\nForma de pago:", str(((len(self.lista[ubi+3]))-1)*"x"))
            return(ubi)

        except:
            print("\nSu nombre no esta en la lista.\n")
            pass


if __name__ == "__main__":
    E = EntradaSalida()
    R = Registro()
    x = E.traductor()
    y = E.ingreso()
    R.buscador(x, y)
