from random import randint


if __name__ == "__main__":
    suma = 0
    for _ in range(10):
        r = randint(0, 9)
        print(r)
        suma += r
    print("promedio: ", suma / 10)