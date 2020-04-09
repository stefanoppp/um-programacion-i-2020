class Calificaciones:

    def __init__(self):
        self.lista = ['Matematica','Lengua','Física','Química','Historia']
        self.nota = [] 

    def listado(self):
        for materia in self.lista:
            self.nota.append(input("¿Que nota se tiene en " + materia + "?\n"))
    
    def imprimir(self):
        for i in range(5):
            print("En", self.lista[i], "tiene un", self.nota[i])
        
def main():
    info = Calificaciones()
    info.listado()
    info.imprimir()
    

if __name__ == "__main__":
    main()