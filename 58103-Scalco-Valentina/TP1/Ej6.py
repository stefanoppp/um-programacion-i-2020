num = int(input("Ingrese un numero\n"))
i = 2
if num != 2:
    while num % i != 0:
        i += 1
if i == num:
    print("El numero ingresado es primo")
else:
    print("El numero ingresado no es primo")