materias = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
for i in materias:
    print(i + " tiene " + str(materias[i]) + " creditos")
    total += materias[i]
print("\nEn total hay {} creditos".format(total))
