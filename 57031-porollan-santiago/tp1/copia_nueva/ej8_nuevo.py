class Asignatura():
    def __init__(self, nota=None, asignatura=None):
        self.nota = nota
        self.asignatura = asignatura
        self.next = None

if __name__ == "__main__":
    alumn = Asignatura()
    first = alumn
    while 1:
        print("detener con stop")
        asignatura = input("asignatura: ")
        if asignatura == "stop":
            break
        nota = input("nota: ")
        if nota == "stop":
            break
        nalumn = Asignatura(nota, asignatura)
        alumn.next = nalumn
        alumn = nalumn
    while first.next is not None:
        first = first.next
        print("En ", first.asignatura, " has sacado ", first.nota)
