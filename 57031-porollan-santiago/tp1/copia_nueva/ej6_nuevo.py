

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

    def es_primo(self):
        for x in range(2, self.valor):
            if self.valor % x == 0:
                return False
        return True


if __name__ == "__main__":
    num = Numero(int(input("numero: ")))
    if num.es_primo():
        print("el numero es primo")
    else:
        print("el numero no es primo")
