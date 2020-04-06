class Curso():
    def __init__(self, materias):
        self.materias = materias

    def getTotal(self):
        return sum(self.materias.values())/len(self.materias)

    def getMaterias(self):
        return self.materias


ejercicio11 = Curso({"Matemáticas": 6, "Física": 4, "Química": 5})

for item in ejercicio11.getMaterias():
    print(item, "tiene", str(ejercicio11.getMaterias()[item]), "creditos")

print("El total de creditos del curso es:", ejercicio11.getTotal())
