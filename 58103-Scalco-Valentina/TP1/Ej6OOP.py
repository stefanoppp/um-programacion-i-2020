class Primos:
    def ident(self, num):
        i = 2
        if num != 2:
            while num % i != 0:
                i += 1
        if i == num:
            return("El numero ingresado es primo")
        else:
            return("El numero ingresado no es primo") 
        

def main():
    num = int(input("Ingrese un numero\n"))
    info = Primos()
    print(info.ident(num))

if __name__ == "__main__":
    main()
