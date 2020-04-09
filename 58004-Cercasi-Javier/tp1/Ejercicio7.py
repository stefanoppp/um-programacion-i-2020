'''Escribir un programa en el que se pregunte al usuario por una frase y una
letra, y muestre por pantalla el número de veces que aparece la letra en
la frase.'''


def interfaz(frase, letra):

    c = 0
    for i in frase:
        if letra == i:
            c += 1
    print("La letra ha aparecido "+str(c)+" veces")


def main():

    frase = (input("Ingrese una frase:\n"))
    letra = input("Ingrese una letra:\n")
    interfaz(frase, letra)


main()
