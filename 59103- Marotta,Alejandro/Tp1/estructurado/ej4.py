def imprimir(altura):
    for i in range(altura+1):
        print("*"*i)


def start():

    altura = int(input("Ingrese la altura del triangulo: "))
    imprimir(altura)


start()
