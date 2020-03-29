frase = input("Ingrese una frase\n")
letr = input("Ingrese una letra\n")
i = 0
for letra in frase:
    if letra == letr:
        i += 1
print("Hay", i,"letras", letr,"en la frase ingresada")