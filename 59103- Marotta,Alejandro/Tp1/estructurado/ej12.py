""" Ejercicio 12
Generar números aleatorios del 1 al 10 y guardar el resultado en un diccionario. Al finalizar
mostrar el resultado del diccionario ordenado de mayor a menor."""

from random import randint

diccionario = {}

for i in range(10):
    
    numero = randint(0,10)

    diccionario[i] = numero

lista = list(diccionario.values())

lista.sort()

print (lista)
