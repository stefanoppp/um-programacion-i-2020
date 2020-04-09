'''Generar 10 números aleatorios, mostrarlos por pantalla y mostrar
el promedio.'''
import random


def logica():

    a = 0
    n = []

    for i in range(10):
        n.append(random.randrange(500))
        a += n[i]

    prom = a/10
    print("\nLos numeros son: ", n)
    print("\nEl promedio de los numeros es : ", prom)


logica()
