class Materias:

    def __init__(self):
        self.curso = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
        self.total = 0

    def totales(self):
        self.total = self.curso["Quimica"] + self.curso["Fisica"] + self.curso["Matematicas"]
    
    def mostrar(self):
        for materia, creditos in self.curso.items():
            print("La asignatura", materia, "tiene", creditos, "creditos")
        print ("El total de creditos es ", self.total)


def main():
    info = Materias()
    info.totales()
    info.mostrar()


if __name__ == "__main__":
    main()