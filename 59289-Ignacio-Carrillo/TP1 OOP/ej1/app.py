from alumno import Alumno
from curso import Curso

class App():

    def __init__(self):
        pass

    def ejecutar(self):
        curso = Curso()
        a = True
        while a == True:
            var = input(("\nDesea ingresar otro alumno?: (Y/N) "))
            if (var == "Y" or var == "y"):
                alumno = Alumno()
                alumno.setNombre()
                alumno.setSexo()
                curso.getRespuesta(alumno.getNombre(), alumno.getSexo())
            else:
                a = False

if __name__ == '__main__':
    app1=App()
    app1.ejecutar()