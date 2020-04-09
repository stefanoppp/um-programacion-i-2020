from ej_10 import Fecha


class Interfaz():

    def interfaz(self):
        x = Fecha()
        date = input("Ingrese la fecha de hoy dia con formato dd/mm/aaaa:\n")
        x.set_date(date)
        fecha = x.fecha(x.get_date())
        meses = x.meses()
        print(str(fecha[0]) + " de " + str(meses[int(fecha[1])]) + " de "
              + str(fecha[2]))


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
