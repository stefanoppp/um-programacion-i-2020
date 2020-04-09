num = 0
while num < 1:
    num = int(input("Ingrese un numero\n"))
for i in range(1, num+1, 2):
    print(i, end=", ")
print(" ")