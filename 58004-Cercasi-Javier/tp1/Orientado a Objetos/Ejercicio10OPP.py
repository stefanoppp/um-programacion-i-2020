'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde
<mes> es el nombre del mes.'''


class Calendario():

    def __init__(self):
        self.meses = []
        self.res = []

    def ingreso(self):
        self.res = input("Dime la fecha en formato dd/mm/aaaa:\n").split('/')
        return(self.res)

    def pantalla(self, res):

        self.meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO",
                      "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE",
                      "DICIEMBRE"]

        print(res[0] + " de " + self.meses[int(res[1])-1] + " de " + res[2])


if __name__ == "__main__":
    C = Calendario()
    res = C.ingreso()
    C.pantalla(res)
