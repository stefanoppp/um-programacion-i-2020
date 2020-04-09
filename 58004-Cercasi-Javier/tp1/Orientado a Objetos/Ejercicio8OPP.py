'''Escribir un programa que almacene las asignaturas de un curso (por
ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura, y después
las muestre por pantalla con el mensaje En <asignatura> has sacado
<nota> donde <asignatura> es cada una des las asignaturas de la lista y
<nota> cada una de las correspondientes notas introducidas por el usuario.'''


class Notas():

    def __init__(self):
        self.materias = ["Matemáticas", "Física", "Química",
                         "Historia", "Lengua"]
        self.notas = []

    def ingreso(self):

        for i in range(5):
            print("Que nota has sacado en "+self.materias[i]+":")
            self.notas.append(input())
        return(self.notas)

    def pantalla(self):

        self.ingreso()
        for j in range(5):
            print("\nEn "+self.materias[j]+" has sacado: "+self.notas[j])


if __name__ == "__main__":
    N = Notas()
    N.pantalla()
