class Ejercicio7():

    def contarLetras(self, frase, letra):
        frase = frase.lower()
        letra = letra.lower()
        return frase.count(letra)


"""
prueba = Ejercicio7()

frase = input("ingrese una frase: ")

letra = input("ingrese una letra: ")

print(prueba.contarLetras(frase, letra))
"""
