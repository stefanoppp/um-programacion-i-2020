import json


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
            v.write("nombre: " + self.nombre + ". apellido: " + self.apellido + ". monto: " + self.monto +
                    ". descripcion: " + self.descripcion + ". metodo: " +self.metodo + "\n")
    
def convertir_a_json():
    data = {}
    for y, line in enumerate(open("venta")):
        d_obj = {}
        L = line.split()
        print(L, y)
        for x in range(5):
            d_obj[inp(x)[:-2]] = L[x*2+1]
        data[y] = d_obj
    with open("venta.json", "w") as v:
        json.dump(data, v, indent=4)


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
    convertir_a_json()
