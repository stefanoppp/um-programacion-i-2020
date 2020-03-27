import random

dicc = {num: random.randint(0, 10) for num in range(20)}

for num in sorted(dicc, key=dicc.get, reverse=True):
    print("El " + str(num) + "º numero que se genero es: " + str(dicc[num]))
