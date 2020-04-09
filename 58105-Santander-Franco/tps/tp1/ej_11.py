class Creditos():
    def __init__(self):
        self.credits = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
        self.subjects = self.credits.keys()

    def suma(self):
        self.suma = 0
        for i in self.credits:
            self.suma += self.credits[i]
        return self.suma


class Interfaz(Creditos):
    def interfaz(self):
        x = Creditos()
        for i in self.subjects:
            print(i + " tiene " + str(self.credits[i]) + " creditos\n")
        print("La suma total de creditos es: ", x.suma())


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
