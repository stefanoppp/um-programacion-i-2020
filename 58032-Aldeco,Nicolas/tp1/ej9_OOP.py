class User():
    def __init__(self):
        self.datos = {
            'Nombre': '',
            'Edad': '',
            'Direccion': '',
            'Telefono': ''
        }
        self.info = self.datos.keys()

    def input_datos(self):
        for dato in self.info:
            temp = input(dato + ' = ')
            self.datos[dato] = temp

    def print_datos(self):
        n = self.datos['Nombre']
        e = self.datos['Edad']
        d = self.datos['Direccion']
        t = self.datos['Telefono']
        print(n+' tiene '+e+' años, vive en '+d+' y su nro de telefono es:'+t)


def main():
    obj = User()
    obj.input_datos()
    obj.print_datos()


if __name__ == '__main__':
    main()
