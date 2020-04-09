curso = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
for materia, creditos in curso.items():
    print("La asignatura", materia, "tiene", creditos, "creditos")
total = curso["Quimica"] + curso["Fisica"] + curso["Matematicas"]
print ("El total de creditos es ", total)