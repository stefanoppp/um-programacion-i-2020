
class Asignatura():

    def __init__(self):

        self.asignatura = ["Matemáticas", "Física","Química","Historia","Lengua"]


    def imprimir(self):
        for clave, valor in self.dic.items(): 
            print ("En la asignatura %s has sacado %s" % (clave, valor))
    


    def asignar(self):
        self.dic= {}
        for x in self.asignatura:
            nota = input("Ingrese la nota obtenida en {} ".format(x))
            self.dic[x] = nota
        print("\n")
    


def start():
    materias = Asignatura()
    materias.asignar()
    materias.imprimir()
    


if __name__ == "__main__":
    start()