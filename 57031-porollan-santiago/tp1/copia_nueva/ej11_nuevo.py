

class Materia():
    def __init__(self, materia=None, creditos=None):
        self.materia = materia
        self.creditos = creditos

    def show(self):
        print(self.materia + " " + str(self.creditos))


if __name__ == "__main__":
    mat = Materia("matematicas", 6)
    fis = Materia("física", 5)
    qui = Materia("quimica", 4)
    total = 0
    mat.show()
    fis.show()
    qui.show()
    print("total del curso: ", mat.creditos + fis.creditos + qui.creditos)
