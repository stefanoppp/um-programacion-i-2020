import random
numeros = []
num = 0
for i in range(10):
    numeros.append(random.randrange(1,11))
    num += numeros[i]
num = num/10
print(numeros)
print("Promedio:", num)
