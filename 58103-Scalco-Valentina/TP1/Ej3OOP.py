class Separation:
    def impar(self, num):
        lista = []
        for i in range(1, num+1, 2):
            lista.append(i) 
        return(lista)
        

def main():
    num = 0
    while num < 1:
        num = int(input("Ingrese un numero\n"))
    info = Separation()
    print(info.impar(num))

if __name__ == "__main__":
    main()
