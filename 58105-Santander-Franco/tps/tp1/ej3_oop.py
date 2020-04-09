class Numero():
    def __init__(self):
        self.num = ''
        self.num2 = []

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def val_num(self, num):
        if num > 0:
            num2 = []
            for i in range(1, num + 1, 2):
                num2.append(i)
            return str(num2).strip("[]")
        else:
            return("Ingrese un numero valido")


if __name__ == "__main__":
    hola = Numero()
