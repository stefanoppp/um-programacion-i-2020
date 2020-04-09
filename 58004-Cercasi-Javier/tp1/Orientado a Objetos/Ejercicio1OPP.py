
# Los Alumnos de un curso se han dividido en dos grupos A y B de acuerdo
# al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre
# anterior a la M y los hombres con un nombre posterior a la N y el grupo B
# por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
# y muestre por pantalla el grupo que le corresponde.


class Alumno():

    def __init__(self):
        self.nombre = ''
        self.gen = ''

    def ingreso(self):

        self.nombre = input("Ingrese su nombre:\n").title()
        self.gen = input("Ingrese su genero:").title()
        return(self.nombre, self.gen)


class Curso():

    def chequeo(self, nombre, gen):

        if not nombre or not gen:
            print("No ingreso los campos obligatorios")

        if ((nombre[0] <= "M" and gen == ("Mujer")) or
           (nombre[0] >= "N" and gen == "Hombre")):

            print("Perteneces al grupo A")

        else:
            print("Perteneces al grupo B")


if __name__ == "__main__":
    A = Alumno()
    B = Curso()
    nombre, gen = A.ingreso()
    B.chequeo(nombre, gen)
