import random 
numeros = {}
for i in range(10):
    numeros.setdefault(random.randrange(1,11), i)
num = sorted(numeros)
num.reverse()
print(num)