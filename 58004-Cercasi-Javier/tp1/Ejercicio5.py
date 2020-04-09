'''Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''


def logica():
    n = ''
    num = int(input("Ingrese un numero entero positivo:\n"))
    for i in range(num):
        n = " "+str((i+1)*2-1)+n
        print(n)


logica()
