class Numero():
    def __init__(self):
        self.num = 0

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def val_num(self, num):
        if num > 0:
            caracter = '*'
            lis = []
            for i in range(0, num + 1):
                lis.append(str(caracter * i))
            return lis
        else:
            return("Ingrese un numero valido")


if __name__ == "__main__":
    hola = Numero()
