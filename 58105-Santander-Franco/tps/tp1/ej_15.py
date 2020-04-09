class Venta():
    def __init__(self, archivo):
        self.archivo = archivo

    def read_line(self):
        for line in self.archivo.readlines():
            print(line)


if __name__ == "__main__":
    archivo = 'venta.txt'
    hola = Venta(archivo)
