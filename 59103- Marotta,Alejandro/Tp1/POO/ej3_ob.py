

class Impares():

    def __init__(self,num):
        self.num = num  
                

    def calcular(self):
        for i in range(1,self.num-1):
            if i%2 > 0 :
                print(i , end=",")
        if (self.num-1)%2 > 0:
            print(self.num-1,end=".")
        if (self.num)%2 > 0:
            print(self.num,end=".")
      
     

def start():
    
    num = int(input("Ingrese un numero positivo: "))

    if num > 0:
        impar = Impares(num)
        impar.calcular()
    else:
        print("El numero no es positivo")
        
    
if __name__ == "__main__":
    
    start()