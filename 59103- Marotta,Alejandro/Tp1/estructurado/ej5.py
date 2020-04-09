def imprimir(altura):
    lista = []
    j=1
    for i in range (altura):
        lista.append(j)
        j +=2
        for i in range(len(lista)-1, -1, -1):
            print(lista[i], end=" ")
        print("\n")
        

def start():
    altura= int(input("Ingrese la altura del triangulo: "))
    imprimir(altura)

start()

