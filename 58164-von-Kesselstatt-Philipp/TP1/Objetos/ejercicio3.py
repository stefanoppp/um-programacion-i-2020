class Number():

    def impar(self, numero):
        result = ""
        for n in range(1, numero, 2):
            result += str(n) + ", "

        return result[:-2]


"""
calculadora = Number()

num = int(input("Ingrese un numero: "))

print(calculadora.impar(num))
"""
