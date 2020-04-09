class Archivo_venta:

    def __init__(self, archivo):
        self.archivo = archivo

    def leer(self):
        print(" ")
        for lineas in self.archivo.readlines():
            linea = lineas.split(",")
            print("Nombre: {}, monto: {},".format(linea[0], linea[1],) +
                  "descripcion: {},".format(linea[2]) +
                  " forma de pago: {}".format(linea[3]))


def main():
    archivo = open("/home/valenscalco/Programacion/um-programacion-i-2020/58103-Scalco-Valentina/Datosventa")
    info = Archivo_venta(archivo)
    info.leer()


if __name__ == "__main__":
    main()