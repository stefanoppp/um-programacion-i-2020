'''Generar números aleatorios del 1 al 10 y guardar el resultado en un
diccionario. Al finalizar mostrar el resultado del diccionario ordenado
de mayor a menor.'''
import random


def logica():

    dic = {}

    for i in range(15):
        dic[i] = random.randrange(1, 10)
    orden = sorted(dic.values(), reverse=True)

    print("Los numeros son :\n", list(dic.values()))
    print("\nLos numeros ordenados de manera descendente: \n", orden)


logica()
