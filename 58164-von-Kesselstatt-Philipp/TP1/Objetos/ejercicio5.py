class Ejercicio5():

    def piramideImpar(self, cantidad):

        for n in range(1, int(cantidad)+1):
            x = ""
            for num in range(1, n*2+1, 2):
                x += str(num)
            print(x[::-1])


"""
prueba = Ejercicio5()

num = int(input("Ingrese un numero  "))

prueba.piramideImpar(num)
"""
