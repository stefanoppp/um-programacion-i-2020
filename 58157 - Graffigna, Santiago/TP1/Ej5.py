
#number = int(input("Ingrese un numero entero a representar\n"))
number = 9

for x in range(1, number + 1, 2):
    for y in range(x, 0, -2):
        print(y, end=" ")

    print(" ")