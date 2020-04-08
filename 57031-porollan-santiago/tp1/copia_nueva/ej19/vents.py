
class TarjetaDeCredito():
    def __init__(self):
        self.nombre = None
        self.numero_tarjeta = None
        self.codigo_verificacion = None
        self.tipo_tarjeta = None


class Ventas():
    def __init__(self):
        self.monto = None
        self.descripcion = None
        self.tarjeta = TarjetaDeCredito()
        self.current = 0
    
    def set_info(self, info):
        if info.lower() == "stop":
            return True
        if self.current == 0:
            self.monto = info
        elif self.current == 1:
            self.descripcion = info
        elif self.current == 2:
            self.tarjeta.nombre = info
        elif self.current == 3:
            self.tarjeta.numero_tarjeta = info
        elif self.current == 4:
            self.tarjeta.codigo_verificacion = info
        elif self.current == 5:
            self.tarjeta.tipo_tarjeta = info
        self.current += 1
        return False

    def write(self):
        with open("ventas", 'a') as vent:
            line =  (self.tarjeta.nombre + " " + self.tarjeta.numero_tarjeta + " " +
                    self.tarjeta.codigo_verificacion + " " + self.tarjeta.tipo_tarjeta + " " +
                    self.monto + " " + self.descripcion)
            print("Escribiendo Datos")
            vent.write(line + "\n")
        