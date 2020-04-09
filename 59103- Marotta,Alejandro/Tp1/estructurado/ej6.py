""" Ejercicio 6 Escribir un programa que pida al usuario un número 
entero y muestre por pantalla si es un número primo o no. """


def primo(num):
    if num < 2:     
        return False
    for i in range(2, num):  
        if num % i == 0:    
            return False
    return True 

def start():
    num = int(input("Ingrese el numero a analizar: "))
    
    if primo(num):
        print("Es primo")
    else:
        print("No es primo")

start()

