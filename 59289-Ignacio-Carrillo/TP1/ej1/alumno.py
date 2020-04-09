class Alumno():

    def __init__(self):
        self.nombre=""
        self.sexo=""

    def setNombre(self):
        self.nombre=input("\nIngrese su nombre: ")
        self.nombre=self.nombre.upper()

    def getNombre(self):
        return self.nombre

    def setSexo(self):
        while True:
            try:
                self.sexo=input("\nIngrese su sexo (M/F): ")
                self.sexo=self.sexo.upper()
                if(self.sexo!='M' and self.sexo!='F'):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\n**ERROR** Introduzca un sexo valido")

    def getSexo(self):
        return self.sexo



