class Ejercicio4():

    def piramide(self, cantidad):

        for n in range(1, cantidad+1):
            x = ""
            for num in range(n):
                x += "*"
            print(x)


"""
prueba = Ejercicio4()

num = int(input("Ingrese un numero  "))

prueba.piramide(num)
"""
