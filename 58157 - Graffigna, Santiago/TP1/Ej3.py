number = int(input("Ingrese un numero entero positivo\n"))
num = 1
print('Numeros Impares:', ', '.join(str(num) for num in range(number + 1) if num % 2))