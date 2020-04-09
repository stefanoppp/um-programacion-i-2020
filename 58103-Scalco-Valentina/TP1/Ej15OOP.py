class Archivo_venta:

    def __init__(self, archivo):
        self.archivo = archivo

    def leer(self):
        print(" ")
        for linea in self.archivo.readlines():
            print(linea)


def main():
    archivo = open("/home/valenscalco/Programacion/um-programacion-i-2020/58103-Scalco-Valentina/Datosventa")
    info = Archivo_venta(archivo)
    info.leer()


if __name__ == "__main__":
    main()