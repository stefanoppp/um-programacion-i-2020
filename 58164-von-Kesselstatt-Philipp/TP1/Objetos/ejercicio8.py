class Curso():
    def __init__(self, materias):
        self.materias = materias
        self.notas = {item: 0 for item in materias}

    def setNotas(self, listaNotas):
        n = 0
        for item in self.materias:
            self.notas[item] = listaNotas[n]
            n += 1

    def getNotas(self):
        return self.notas


"""
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
mks = [input("Ingrese su nota en " + mat + " ") for mat in materias]


ejercicio8 = Curso(materias)
ejercicio8.setNotas(mks)

for item in ejercicio8.getNotas():
    print("En", item, "has sacado", ejercicio8.getNotas()[item])
"""
