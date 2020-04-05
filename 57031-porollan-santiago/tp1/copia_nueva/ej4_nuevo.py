

class Numero():
    def __init__(self, num):
        self.valor = num
    
    def obtener_impares(self):
        return [str(x) for x in range(self.valor + 1) if x%2 == 1]

    def get_x(self):
        return ["*"*x for x in range(1, self.valor+1)]

if __name__ == "__main__":
    num = Numero(int(input("rango: ")))
    for line in num.get_x():
        print(line)
