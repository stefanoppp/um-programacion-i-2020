from ej4_oop import Numero


class Interfaz():
    def interfaz(self):
        valor = Numero()
        num = int(input("Ingrese un numero entero positivo\n"))
        valor.set_num(num)
        numero = valor.get_num()
        lis = valor.val_num(numero)
        print("Su triangulo es:\n")
        for i in lis:
            print(i)


if __name__ == "__main__":
    Interfaz = Interfaz()
    Interfaz.interfaz()
