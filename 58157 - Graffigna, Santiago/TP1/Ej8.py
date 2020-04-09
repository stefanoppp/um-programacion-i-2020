from os import system

materias = ["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
print("Ingrese sus notas de Matematica, Fisica, Quimica, Historia y Lengua respectivamente")

for materia in materias:
    nota = int(input())
    notas.append(nota)

system('clear')    
i = 0
for materia in materias:
    print("En", materias[i].upper(), "has sacado:", notas[i])
    i += 1
