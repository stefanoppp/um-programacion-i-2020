lista = ['Matematica','Lengua','Física','Química','Historia']
notas = []
for materia in lista:
    notas.append(input("¿Que nota se tiene en " + materia + "?\n"))
for i in range(len(lista)):
    print("En", lista[i], "tiene un", notas[i])