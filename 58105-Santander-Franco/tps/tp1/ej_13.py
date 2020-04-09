from random import randint


class Number():
    def __init__(self):
        self.numbers = []
        self.prom = 0
        self.nota = 0

    def generator(self):
        for i in range(10):
            self.numbers.append(randint(1, 10))
        self.prom = 0
        for i in self.numbers:
            self.prom += i
        self.nota = self.prom / 10
        return self.numbers, self.nota


class Interfaz(Number):
    def interfaz(self):
        x = Number()
        a, b = x.generator()
        print("Las notas son:\n", a)
        print("El promedio total es: ", b)


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
