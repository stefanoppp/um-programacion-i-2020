import json
from ej15_escribir_venta import inp

if __name__ == "__main__":

    data = {}
    for y, line in enumerate(open("venta")):
        d_obj = {}
        L = line.split()
        for x in range(5):
            d_obj[inp(x)[:-2]] = L[x]
        data[y] = d_obj
    with open("venta.json", "w") as v:
        json.dump(data, v, indent=4)
