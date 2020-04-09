from ejercicio_8 import Subject


class Interfaz():

    def interfaz(self):
        x = Subject()
        num = int(input("Ingrese el numero de materias que desea ingresar:\n"))
        a, b = x.lis(num)
        x.set_subjects(a)
        x.set_notes(b)
        notas = x.get_notes()
        materias = x.get_subjects()
        for i in range(0, len(materias)):
            print("En " + str(materias[i]) + " has sacado " + str(notas[i]))


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
