name = input("Ingrese su nombre: ")
sex = input("Ingrese su sexo m o f: ")

abc = ['a', 'b', 'c', 'd', 'e', 'f',
       'g', 'h', 'i', 'j', 'k', 'l',
       'm', 'n', 'ñ', 'o', 'p',
       'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z']

if (sex == "f" and abc.index(name[0].lower()) < 12 or
   sex == "m" and abc.index(name[0].lower()) > 13):
    print("Usted pertenece al grupo A")
else:
    print("Usted pertenece al grupo B")
