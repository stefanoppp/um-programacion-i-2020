class Venta():
    def __init__(self, archivo):
        self.archivo = archivo
        self.dicc = {}
        self.ventas = {}

    def read_line(self):
        i = 1
        for line in self.archivo.readlines():
            try:
                lista = line.split(",")
                if "" in lista:
                    raise ErrorDatoNulo
                self.ventas = {"Nombre": str(lista[0]),
                               "Monto": str(lista[1]),
                               "Especificacion": str(lista[2]),
                               "Forma de pago":
                               str(lista[3].replace('\n', '')
                                   )}
                self.dicc['venta numero' + str(i)] = self.ventas
                i += 1
            except ErrorDatoNulo:
                print("\n\nOcurrió un problema con la fuente de datos\n\n")
                continue
        return self.dicc


class ErrorDatoNulo(Exception):
    pass


if __name__ == "__main__":
    archivo = 'venta.txt'
    hola = Venta(archivo)
