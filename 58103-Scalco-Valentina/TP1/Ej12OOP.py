import random

class Aleatorio:
    def create(self, numeros):
        for i in range(10):
            numeros.setdefault(random.randrange(1,11), i)
        return(numeros)
        
def main():
    numeros = {}
    info = Aleatorio()
    num = sorted(info.create(numeros))
    num.reverse()
    print(num)

if __name__ == "__main__":
    main()