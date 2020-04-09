
class Triangulo():

    def imprimir(self,altura):
        for i in range (altura+1):
            print ("*"*i)


def main():
    altura= int(input("Ingrese la altura del triangulo: "))
    triangulo = Triangulo()
    triangulo.imprimir(altura)

if __name__ == "__main__":
    main()