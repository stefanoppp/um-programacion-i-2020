class Subject():

    def __init__(self):
        self.subjects = []
        self.notes = []

    def get_subjects(self):
        return self.subjects

    def set_subjects(self, subjects):
        self.subjects = subjects

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def lis(self, num):
        materia = ''
        nota = 0
        lis_mate = []
        lis_note = []
        for i in range(0, num):
            materia = input("Ingrese el nombre de la materia:\n")
            nota = input("Ingrese la nota correspondiente a la materia:\n")
            lis_mate.append(materia)
            lis_note.append(nota)
        return lis_mate, lis_note


if __name__ == "__main__":
    hola = Subject()
