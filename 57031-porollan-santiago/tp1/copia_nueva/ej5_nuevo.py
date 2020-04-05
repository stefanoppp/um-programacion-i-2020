

class Numero():
    def __init__(self, num):
        self.valor = num
    
    def obtener_impares(self):
        return [str(x) for x in range(self.valor + 1) if x%2 == 1]

    def get_x(self):
        return ["*"*x for x in range(1, self.valor+1)]

    def p(self, r, l, c):
        if c != -1:
            print(l[c:])
            self.p(r, l, c-1)

    def get_l(self, r):
        a = 1
        l = []
        for _ in range(1, r+1):
            l.insert(0, a)
            a+=2
        return l


if __name__ == "__main__":
    num = Numero(int(input("rango: ")))
    num.p(num.valor, num.get_l(num.valor), num.valor-1)
