

class Numero():
    def __init__(self, num):
        self.valor = num
    
    def obtener_impares(self):
        return [str(x) for x in range(self.valor + 1) if x%2 == 1]


if __name__ == "__main__":
    num = Numero(int(input("rango: ")))
    print("impares hasta el " + str(num.valor) + ": " + ", ".join(num.obtener_impares()))
        