class TarjetaCredito():
    def __init__(self, name, cardnumber, code, tipo):
        self.name = name
        self.cardnumber = cardnumber
        self.code = code
        self.type = tipo

    def get_name(self):
        return self.name

    def get_cnumber(self):
        return self.cardnumber

    def get_code(self):
        return self.code

    def get_type(self):
        return self.type


class Venta():
    def __init__(self, archivo):
        self.archivo = archivo
        self.dicc = {}
        self.ventas = {}

    def get_cash(self):
        return self.cash

    def set_cash(self, cash):
        self.cash = cash

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    # def dicc(self, linea, tarjta):
        # dic
    def datos2(self):
        i = 1
        for line in self.archivo.readlines():
            try:
                lista = line.split(",")
                if "" in lista:
                    raise ErrorDatoNulo
                card = TarjetaCredito(str(lista[0]), str(lista[1]),
                                      str(lista[2]), str(lista[3]))
                self.set_cash(lista[4])
                self.set_description(lista[5].replace('\n', ''))
                self.ventas = {"Nombre y Apellido": card.get_name(),
                               "Numeor de Tarjeta de "
                               "Credito": card.get_cnumber(),
                               "Codigo de verificacion": card.get_code(),
                               "Tipo de tarjeta de credito": card.get_type(),
                               "Monto de la venta": self.get_cash(),
                               "Descripcion de la venta": self.get_description(
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
