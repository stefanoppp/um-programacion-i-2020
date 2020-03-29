def impar(numero):
    result = ""
    for n in range(1, numero, 2):
        result += str(n) + ", "

    return result[:-2]


# print(impar(int(input("Ingrese un numero: "))))
