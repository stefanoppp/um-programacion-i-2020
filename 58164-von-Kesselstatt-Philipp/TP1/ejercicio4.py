cantidad = input("ingrese un numero")

for n in range(1, int(cantidad)+1):
    x = ""
    for num in range(n):
        x += "*"
    print(x)
