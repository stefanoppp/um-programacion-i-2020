class Alumno():

    def __init__(self):
        self.name = ''
        self.sex = ''

    def set_name(self, name):
        self.name = name

    def set_sex(self, sex):
        self.sex = sex

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex


class Course():

    def define_course(self, sex, name):
        if sex[0] == "m" or sex[0] == "f":
            if sex[0] == "m":
                if name[0] <= "n":
                    return("Pertenece al curso B")
                else:
                    return("Pertenece al curso A")
            else:
                if name[0] <= "l":
                    return("Pertenece al curso A")
                else:
                    return("Pertenece al curso B")
        else:
            return("Ingrese un sexo valido")


class Interfaz():

    def interfaz(self):
        alumno = Alumno()
        curso = Course()
        name = str(input("Ingrese su nombre:\n"))
        sex = str(input("Ingrese su sexo:\n-femenino\n-masculino\n"))
        alumno.set_name(name.lower())
        alumno.set_sex(sex)
        nombre = alumno.get_name()
        sexo = alumno.get_sex()
        print(curso.define_course(sexo, nombre))


if __name__ == '__main__':

    Interfaz = Interfaz()
    Interfaz.interfaz()
