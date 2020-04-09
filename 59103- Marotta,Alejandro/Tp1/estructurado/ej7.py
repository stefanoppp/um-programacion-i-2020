""" Ejercicio 7 
Escribir un programa en el que se pregunte al usuario por una frase 
y una letra, y muestre por pantalla el número de veces que aparece 
la letra en la frase. """

def contar(frase,letra):
    cantidad = frase.count(letra)
    return cantidad

def start():
    frase = input("Ingrese una frase y toque enter: \n")
    letra = input("¿Que letra desea saber cuantas veces se repite?\n")

    frase = frase.lower() #Para que no importe si esta en minuscula o mayuscula
    letra = letra.lower()


    cantidad = contar(frase,letra)

    print("\n")
    print("La letra {} se repite {} veces".format(letra,cantidad))

start()