import os
import json

class Excepcionador():

    def __init__(self):

        self.file = open('sales.txt', 'r')
        self.json = open('ARCHIVO_ORIGINAL18.json', 'w')

    def exceptionator(self):

        sales_dicctionary = {}
        identifiers = ["Nombre", "Monto", "Descripcion", "Forma De Pago"]

        with open('sales.txt', 'r') as f1:
            with open('ARCHIVO_ORIGINAL18.json', 'w') as f2:

                for line in f1:
                    line = line.split(",")

                    for x in range(0, 4):

                        if "\n" in line[x] != -1:
                            line[x] = line[x].rstrip("\n")

                        if line[x] == "":
                            raise Exception("ERROR 404")

                        sales_dicctionary.update({identifiers[x]: [line]})

                    json.dump(sales_dicctionary, f2)
                    f2.write("\n")


if __name__ == "__main__":
    start = Excepcionador()
    start.exceptionator() 