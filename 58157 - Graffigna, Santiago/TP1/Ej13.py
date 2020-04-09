import random

class Randomizer():
 
    def __init__(self):
        self.list = []

    def average(self):
        self.list = random.sample(range(1, 101), 10)
        return sum(self.list) / len(self.list)


def mostrar():
    show = Randomizer()
    average = show.average()
    print(show.list, "\n\nEl promedio total es: ", average)

if __name__ == "__main__":
    mostrar()