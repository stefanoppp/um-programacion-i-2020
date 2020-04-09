


class Triangulo():
    
    def __init__(self,altura):
        
        self.lista = []
        j=1
        for i in range (altura):
            self.lista.append(j)
            j +=2
            for i in range(len(self.lista)-1, -1, -1):
                print(self.lista[i], end=" ")
            print("\n")
        

def main():
    altura= int(input("Ingrese la altura del triangulo: "))
    triangulo = Triangulo(altura)

if __name__ == "__main__":
    main()