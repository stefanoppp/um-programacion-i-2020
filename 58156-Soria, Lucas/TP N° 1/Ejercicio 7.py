frase = input("Ingrese una frase: ").replace("", ",").strip(",").split(",")
letra = input("Ingrese una letra: ")
print("La cantidad de letras {} en la frase es: {}".format(letra, frase.count(letra)))
