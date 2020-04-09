num = int(input("Ingrese un numero entero positivo\n"))
if num >= 0:
    num2 = []
    for i in range(1, num + 1, 2):
        num2.append(i)
    print("Los numeros son impares hasta el numero "
          "ingresado son:", str(num2).strip("[]"))
else:
    print("Ingrese un numero valido")
