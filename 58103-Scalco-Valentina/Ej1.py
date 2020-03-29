nombre = input("Ingrese su nombre \n")
gen = int(input("Ingrese 1 si es mujer y 2 si es hombre \n"))
letra = nombre[0]
alfa1 = "AaBbCcDdEeFfGgHhIiJjKkLl"
alfa2 = "OoPpQqRrSsTtUuVvWwXxYyZz"
if gen == 1:
    if letra in alfa1:
        print("Usted pertenece al Grupo 1")
    else:
        print("Usted pertenece al Grupo 2")    
else:
    if letra in alfa2:
        print("Usted pertenece al Grupo 1")
    else:
        print("Usted pertenece al Grupo 2")
