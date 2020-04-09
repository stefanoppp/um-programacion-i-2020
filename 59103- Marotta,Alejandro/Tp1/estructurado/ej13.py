""" Ejercicio 13
Generar 10 números aleatorios, mostrarlos por pantalla y mostrar el promedio.
 """

from random import randint

promedio = 0

for i in range(10):    
   
    numero = randint(0,10)

    print(numero)

    promedio = promedio + numero

print(promedio/10)

    