def ejercicio6(number):
    prim = True

    if number < 2:
        return "El numero no es primo"

    for num in range(2, number-1):
        if number % num == 0:
            prim = False
            break
        else:
            prim = True

    if prim:
        return "El numero es primo"
    else:
        return "El numero no es primo"


print(ejercicio6(int(input("ingrese un numero: "))))
