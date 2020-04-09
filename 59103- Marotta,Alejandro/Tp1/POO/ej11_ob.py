

class Asignaturas():

    def __init__(self):
        self.asignaturas = {}

    def almacenar(self,key,value):
        self.asignaturas [key] = int(value)

    def imprimir(self):
        for key in self.asignaturas:
            print(key, " tiene ", self.asignaturas[key], " creditos. \n")

    def creditos(self):
        total = 0
        for key in self.asignaturas:
            total = total + self.asignaturas[key]
        print ("El curso tiene {} creditos".format(total))

    

    def pedir(self):
        nombre = input("Ingrese la asignatura: ")
        cred = input("Ingrese los creditos: ")
        self.almacenar(nombre,cred)


    def start(self):
        seguir = True
    
        while seguir == True:
            self.pedir()

            a = input("Desea seguir agregando asignaturas S/N : ")
        
            if a == "N":
                seguir = False

        print("\n")

        self.imprimir()
        self.creditos()


def main():

    ejercicio = Asignaturas()
    ejercicio.start()

if __name__ == "__main__":
    main()