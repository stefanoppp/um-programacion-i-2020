number = int(input("ingrese un numero: "))

for num in range(2, number-1):
    if number % num == 0:
        prim = False
        break
    else:
        prim = True

if prim:
    print("El numero es primo")
else:
    print("El numero no es primo")
