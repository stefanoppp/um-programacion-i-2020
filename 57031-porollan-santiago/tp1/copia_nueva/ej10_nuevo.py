

class Fecha():
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    
    def formatear_mes(self):
        return Meses[self.mes]


Meses = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio" ,
     7:"julio" ,8:"agosto" ,9:"septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}


if __name__ == "__main__":
    dia = input("dia: ")
    mes = input("mes: ")
    año = input("año: ")
    fecha = Fecha(int(dia), int(mes), int(año))
    print(fecha.dia, " de ", fecha.formatear_mes(), " de ", fecha.año)
