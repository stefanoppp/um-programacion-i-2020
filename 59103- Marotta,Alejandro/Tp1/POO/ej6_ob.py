
class Primo():

    def __init__(self,num):
        self.num = int(num)



    def primo(self):
        if self.num < 2:     
            return False
        for i in range(2, self.num):  
            if self.num % i == 0:    
                return False
        return True 

    def imprimir(self):        
    
        if self.primo():
            print("Es primo")
        else:
            print("No es primo")

def main():

    num = input("Ingrese un numero entero y veremos si es primo ")

    primo = Primo(num)

    primo.imprimir()

if __name__ == "__main__":
    main()


