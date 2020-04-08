

class Pago():
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.monto=None
        self.descripcion=None
        self.metodo=None
    
    def set_value(self, info):
        if info == "stop":
            return False
        elif not self.nombre:
            self.nombre = info
        elif not self.apellido:
            self.apellido = info
        elif not self.monto:
            self.monto = info
        elif not self.descripcion:
            self.descripcion = info
        elif not self.metodo:
            self.metodo = info
        return True
    
    def write(self):
        with open("venta", 'a') as v:
            v.write(self.nombre + " " + self.apellido + " " + self.monto +
                    " " + self.descripcion + " " +self.metodo + "\n")


def inp(idx):
    if idx == 0:
        return "nombre: "
    elif idx == 1:
        return "apellido: "
    elif idx == 2:
        return "monto: "
    elif idx == 3:
        return "descripción: "
    elif idx == 4:
        return "metodo de pago: "


if __name__ == "__main__":
    print("stop para terminar")
    stop = True
    while stop:
        pago = Pago()
        count = 0
        while count < 5:
            stop = pago.set_value(input(inp(count)))
            if stop:
                count += 1
            else:
                break
            if count == 5:
                pago.write()

    for line in open("venta"):
        print(line.rstrip())
