
class Alumno():

    def __init__(self,sexo,nombre):
        
        self.sexo = sexo
        self.nombre = nombre
    

    def separar(self):
        if (self.sexo == "M" and self.nombre[0]<= "M") or (self.sexo == "H" and self.nombre[0]>= "N"):
            print("Pertenece al Grupo A")
        else:
            print("Pertenece al Grupo B")


def main():

    sexo = input("Ingrese H si es hombre o M si es mujer: \n")
    nombre = input("Ingrese su nombre: ")

    alumno = Alumno(sexo,nombre)
    alumno.separar()

if __name__ == "__main__":
    main()


