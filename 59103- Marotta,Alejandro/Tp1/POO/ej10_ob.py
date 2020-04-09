

class Fecha():
    
    def __init__(self):

        self.meses = {"01": "Enero","02": "Febrero","03": "Marzo","04": "Abril","05": "Mayo",
                "06": "Junio","07": "Julio","08": "Agosto","09": "Septiembre","10": "Octubre","11": "Noviembre","12": "Diciembre"}

    def ingreso(self,fecha):

        lista = fecha.split("/")

        return lista

    def mostrar(self,lista):
        
        print("La fecha es {} de {} del {}".format(lista[0],self.meses[lista[1]],lista[2]))


def main():

    objeto = Fecha()
    fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
    objeto.mostrar(objeto.ingreso(fecha))


if __name__ == "__main__":
    main()




