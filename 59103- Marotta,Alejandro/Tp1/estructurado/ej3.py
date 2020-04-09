""" Ejercicio 3 Escribir un programa que pida al usuario un número entero positivo y
 muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas. """


def positivo(num):
    if num > 0:
        impares(num)
    else:
        print("El numero no es positivo")


def impares(num):
    for i in range(1, num-1):
        if i%2 > 0 :
            print(i , end=",")
    if (num-1)%2 > 0:
        print(num-1,end=".")
    if (num)%2 > 0:
        print(num,end=".")
        
        
def start():
    num = int(input("Ingrese un numero positivo: "))
    positivo(num)


start()


