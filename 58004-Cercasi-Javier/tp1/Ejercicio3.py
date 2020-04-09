# Escribir un programa que pida al usuario un número entero positivo y muestr
# por pantalla todos los números impares desde 1 hasta ese número separados
# por comas.


def interfaz():
    num = int(input("Ingrese un numero entero positivo:\n"))
    n = ''
    for i in range(1, num, 2):
        n = n+str(i)+","

    print("Los numeros impares son: "+n)


interfaz()
