class Usuario():

    def __init__(self):
        self.nombre=""
        self.edad=0
        self.direccion=""
        self.telefono=""

    def setNombre(self):
        self.nombre=input("\nIngrese su nombre: ")
        self.nombre=self.nombre.upper()
    
    def setEdad(self):
        while True:
            try:
                self.edad=int(input("\nIngrese su edad: "))
                if self.edad<0 and self.edad>100:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nLa edad ingresada es invalida. Intente nuevamente")

    def setDireccion(self):
        self.direccion=input("\nIngrese su direccion: ")
        self.direccion=self.direccion.capitalize()

    def setTelefono(self):
        while True:
            try:
                self.telefono=input("\nIngrese su telefono (Ej: 261-3456789): ")
                if len(self.telefono)!=11:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nEl telefono ingresado es invalido. Intente nuevamente")
    
    def getNombre(self):
        return self.nombre.capitalize()
    
    def getEdad(self):
        return self.edad

    def getDireccion(self):
        return self.direccion.capitalize()
    
    def getTelefono(self):
        return self.telefono
