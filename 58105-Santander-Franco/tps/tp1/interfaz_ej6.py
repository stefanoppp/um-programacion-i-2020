from ejercicio_6 import Numero


class Interfaz():

    def interfaz(self):
        valor = Numero()
        num = int(input("Ingrese numero entero positivo mayor a 2 para ver "
                        "si es primo o no\n"))
        valor.set_num(num)
        numero = valor.get_num()
        print(valor.val_num(numero))


if __name__ == "__main__":
    Interfaz = Interfaz()
    Interfaz.interfaz()
