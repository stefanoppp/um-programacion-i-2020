import random

veces = int(input("Ingrese la cantidad de numeros que quiere generar: "))
num = {}
for i in range(veces):
    num[i] = random.randint(1,10)

nume = dict(sorted(num.items()))
'''
li = sorted(num.values())
for i in num:
    num[i] = li[i]
    print(num[i])
'''
print(nume)