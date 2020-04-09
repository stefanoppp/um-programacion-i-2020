class Date:
    def __init__(self):
        self.fecha = []
        self.mes = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio',
                    8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

    def convertir(self, fecha):
        self.fecha = fecha.split("/")
        return self.fecha

def main():
    info = Date()
    fecha = info.convertir(input("Ingrese la fecha en formato dd/mm/aaaa\n"))
    print("La fecha introducida es:", fecha[0], "de", info.mes[int(fecha[1])], "de", fecha[2])


if __name__ == "__main__":
    main()