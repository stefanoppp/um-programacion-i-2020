result = ""
for n in range(1, int(input("Ingrese un numero: ")), 2):
    result += str(n) + ", "

print(result[:-2])
