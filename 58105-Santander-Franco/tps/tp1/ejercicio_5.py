class Numero():
    def __init__(self):
        self.num = 0

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def val_num(self, num):
        if num > 0:
            return True
        else:
            return("Ingrese un numero valido")


if __name__ == "__main__":
    hola = Numero()
