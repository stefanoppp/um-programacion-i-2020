

class Persona():



    def __init__(self,nombre,edad,direc,tel):

        self.dic = {"nombre":nombre,"edad":edad,"direccion":direc,"telefono":tel }    
        

    def imprimir(self):

        print("{} tiene {} años, vive en {} y su numero de telefono es {}".format(self.dic["nombre"],self.dic["edad"],self.dic["direccion"],self.dic["telefono"]))

def start():
    
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    direc = input("Ingrese su direccion: ")
    telefono = input("Ingrese su telefono: ")

    persona = Persona(nombre,edad,direc,telefono)
    persona.imprimir()

if __name__ == "__main__":
    start()