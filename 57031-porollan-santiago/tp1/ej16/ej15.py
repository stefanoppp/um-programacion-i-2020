

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
    with open("venta", 'w') as v:
        while 1:
            line = ""
            for idx in range(5):
                etiqueta = inp(idx)
                info = input(etiqueta)
                if info == "stop":
                    break
                line += " " + etiqueta + info
            if info == "stop":
                break
            v.write(line + "\n")
    for line in open("venta"):
        print(line.rstrip())