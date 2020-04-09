from random import randint


class Numeros():
    def show(self):
        suma = 0
        for _ in range(10):
            r = randint(0, 9)
            print(r)
            suma += r
        print("promedio: ", suma / 10)


if __name__ == "__main__":
    num = Numeros()
    num.show()
    
