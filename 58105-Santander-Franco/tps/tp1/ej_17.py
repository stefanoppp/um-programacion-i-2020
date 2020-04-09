class Venta():
    def __init__(self, archivo):
        self.archivo = archivo
        self.lista = []
        self.dicc = {}
        self.ventas = {}

    def read_line(self):
        i = 1
        for line in self.archivo.readlines():
            self.lista = line.split(",")
            self.ventas = {"Nombre": str(self.lista[0]),
                           "Monto": str(self.lista[1]),
                           "Especificacion": str(self.lista[2]),
                           "Forma de pago": str(self.lista[3].replace('\n', '')
                                                )}
            self.dicc['venta numero' + str(i)] = self.ventas
            i += 1
        return self.dicc


if __name__ == "__main__":
    archivo = 'venta.txt'
    hola = Venta(archivo)
