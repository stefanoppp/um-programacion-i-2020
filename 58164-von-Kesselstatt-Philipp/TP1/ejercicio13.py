import random

total = 0

for i in range(10):
    x = random.randint(0, 10)
    print(x)
    total += x
    x = 0

print("promedio: " + str(total/10))
