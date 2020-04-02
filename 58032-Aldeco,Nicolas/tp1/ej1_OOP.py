class Alumno():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    @property
    def get_name(self):
        return self.name

    @property
    def get_sex(self):
        return self.sex


class Group_Definer():

    def get_group(self, name, sex):
        aplha = list(map(chr, range(97, 123)))
        index = aplha.index(name[0].lower())
        if not name.isalpha():
            return('bad_name_input')
        if sex.lower() == 'f':
            if index < 13:
                return('GRUPO A')
            else:
                return('GRUPO B')
        elif sex.lower() == 'm':
            if index >= 13:
                return('GRUPO A')
            else:
                return('GRUPO B')
        else:
            return('bad_sex_input')


def main():
    grupo = Group_Definer()
    name = input('Nombre>>')
    sex = input('Sexo(m o f)>>')
    tipazo = Alumno(name, sex)
    nombre = tipazo.get_name
    sexo = tipazo.get_sex
    print(grupo.get_group(nombre, sexo))


if __name__ == '__main__':
    main()
