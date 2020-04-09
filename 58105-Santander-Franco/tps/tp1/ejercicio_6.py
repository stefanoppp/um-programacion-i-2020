class Numero():

    def __init__(self):
        self.num = 0

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def val_num(self, num):
        if num > 2:
            i = 2
            while num % i != 0:
                i += 1
            if i == num:
                return("El numero " + str(num) + " es primo")
            else:
                return("El numero " + str(num) + " no es primo")
        else:
            return("Ingrese un numero valido")


if __name__ == "__main__":
    hola = Numero()
