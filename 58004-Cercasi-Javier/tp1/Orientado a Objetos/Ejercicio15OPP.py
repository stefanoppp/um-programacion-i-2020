'''Crear un programa que lea un archivo de lista que va a contener datos
de una venta y mostrarlo por pantalla. El formato será:
Nombre y apellido, monto de la venta, descripción, forma de pago
(contado o tarjeta). El archivo contendrá una línea por cada venta,
y podrá contener múltiples ventas.'''


class EntradaSalida():

    def __init__(self):

        self.lista = []
        self.nombre = ''
        self.texto = ''
        self.datos = open("/home/javi/Programacion_1/um-programacion-i-" +
                          "2020/58004-Cercasi-Javier/tp1/Ejercicio15.txt", "r")

    def traductor(self):

        self.texto = self.datos.read().replace("\n", ",")
        self.lista = list(self.texto.strip().split(","))
        return(self.lista)

    def ingreso(self):
        self.nombre = input("Ingrese el nombre y apellido para obtener sus " +
                            "datos:\n").title()
        return(self.nombre)


class Registro():

    def buscador(self, x, y):
        self.lista = x
        self.nombre = y

        try:
            ubi = self.lista.index(self.nombre)
            print("\nSus datos son:\n\nNombre:", self.lista[ubi],
                  "\nMonto de la venta:", self.lista[ubi+1],
                  "\nDescripcion:", self.lista[ubi+2], "\nForma de pago:",
                  self.lista[ubi+3])

        except:
            print("\nSu nombre no esta en la lista.\n")
            pass


if __name__ == "__main__":
    E = EntradaSalida()
    R = Registro()
    x = E.traductor()
    y = E.ingreso()
    R.buscador(x, y)
