genero = input("Enter your gender (H o M) : ")
genero = genero.upper()
name = input("Enter your name : ")
name = name.upper()
allowed_GroupA_M = 'abcdefghijkl'
allowed_GroupA_H = 'opqrstuvwxyz'

if genero == 'M':
    if any(name.startswith(x) for x in allowed_GroupA_M):
        print(name, "estas en el GRUPO A!")
    else:
        print(name, "estas en el GRUPO B!")
else:
    if any(name.startswith(x) for x in allowed_GroupA_H):
        print(name, "estas en el GRUPO A!")
    else:
        print(name, "estas en el GRUPO B!")