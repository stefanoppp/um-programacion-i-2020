

class Alumno():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.set_group()
        
    def set_group(self):
        if sex == "f" and (ord(name[0]) < 109) or sex == "m" and (ord(name[0]) > 110):
            self.group = "grupo A"
        else:
            self.group = "grupo B"


if __name__ == "__main__":
    name = input("ingresar nombre: ")
    sex = input("ingresar sexo (m f): ")
    persona = Alumno(name, sex)
    print(persona.group)
