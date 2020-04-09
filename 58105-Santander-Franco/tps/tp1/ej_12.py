from random import randint


class Numbers():
    def __init__(self):
        self.numbers = {}

    def generator(self):
        for i in range(10):
            self.numbers[i] = randint(1, 10)
        return(self.numbers)

    def get_numbers(self):
        return self.numbers

    def sortDictioary(self):
        return sorted(self.numbers, key=self.numbers.get, reverse=True)


if __name__ == "__main__":
    hola = Numbers()
    hola.generator()
    print("El orden de mayor a menor de los numeros creados es:\n")
    for i in hola.sortDictioary():
        print(str(i+1) + " : " + str(hola.get_numbers()[i]))
