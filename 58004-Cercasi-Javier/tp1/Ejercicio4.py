# Escribir un programa que pida al usuario un número entero positivo y
# muestre por pantalla todos los números impares desde 1 hasta ese número
# separados por comas.


def interfaz():
    num = int(input("Ingrese un numero entero positivo:\n"))
    for i in range(num+1):
        print(i*"*")


interfaz()
