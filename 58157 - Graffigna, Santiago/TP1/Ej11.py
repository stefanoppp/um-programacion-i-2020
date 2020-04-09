
creditos_asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 4}

for asignatura, creditos in creditos_asignaturas.items():
    print("La asignatura", asignatura.upper(), "tiene", creditos, "creditos\n")

creditos_totales = creditos_asignaturas['Matematicas'] + creditos_asignaturas['Fisica'] + creditos_asignaturas['Quimica']
print("Total de creditos del cursado:", creditos_totales, "\n")
