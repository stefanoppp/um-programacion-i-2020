from ej3_oop import Numero


class Interfaz():
    def interfaz(self):
        valor = Numero()
        num = int(input("Ingrese un numero entero positivo\n"))
        valor.set_num(num)
        numero = valor.get_num()
        total = valor.val_num(numero)
        print("Los numeros impares hasta el numero "
              "ingresado son:", total)


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
