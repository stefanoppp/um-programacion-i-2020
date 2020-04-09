from ejercicio_5 import Numero


class Interfaz():

    def interfaz(self):
        valor = Numero()
        num = int(input("Ingrese un numero entero positivo \n"))
        valor.set_num(num)
        numero = valor.get_num()
        val = valor.val_num(numero)
        if val is True:
            print("Su triangulo es:\n")
            for i in range(1, num + 1, 2):
                for j in range(i, 0, -2):
                    print(j, end=" ")
                print("")


if __name__ == "__main__":
    Interfaz = Interfaz()
    Interfaz.interfaz()
