class Alumno():

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSex(self):
        return self.sex

    def setSex(self, sex):
        self.sex = sex


class GroupSelectApp():

    def grupo(self, alumno):
        abc = ['a', 'b', 'c', 'd', 'e', 'f',
               'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'ñ', 'o', 'p',
               'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

        if (
            alumno.sex == "f" and abc.index(alumno.name[0].lower()) < 12 or
            alumno.sex == "m" and abc.index(alumno.name[0].lower()) > 13
                ):

            return "Usted pertenece al grupo A"
        else:
            return "Usted pertenece al grupo B"


"""
app = GroupSelectApp()

name = input("Ingrese su nombre: ")
sex = input("Ingrese su sexo m o f: ")

alumno_1 = Alumno(name, sex)

print(app.grupo(alumno_1))
"""
