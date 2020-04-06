

class ValorVacio(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ValorVacio, {0} '.format(self.message)
        else:
            return 'Dato vacío. Reiniciando ingreso de datos'


class Stop(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Stop, {0} '.format(self.message)
        else:
            return 'Deteniendo ingreso de datos'


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
    print(" \"stop\" para terminar")
    with open("venta", 'w') as v:
        pass
    while 1:
        line = ""
        for idx in range(5):
            info = input(inp(idx))
            try:
                if info == "":
                    raise ValorVacio()
                elif info == "stop":
                    raise Stop()
            except ValorVacio as v:
                print(v)
                break
            except Stop as s:
                print(s)
                break
            else:
                line += " " + info
        if info == "stop":
            break
        if info == "":
            continue
        print("Se ha almacenado la información")
        with open("venta", "a") as v:
            v.write(line + "\n")

    print("Mostrando Datos")
    for line in open("venta"):
        print(line.rstrip())