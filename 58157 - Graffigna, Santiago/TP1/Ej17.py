import json

class Creator():

    def __init__(self):

        self.file = open('sales.txt', 'r')
        self.json = open('ARCHIVO_ORIGINAL.json', 'w')

    def convert_to_dot_json(self):

        with open('ARCHIVO_ORIGINAL.json', 'w') as f:
            sales_dicctionary = {}
            identifiers = ["Nombre", "Monto", "Descripcion", "Forma De Pago"]
 
            for line in self.file:
                sales = line.split(',')
                ref = 0

                for item in sales:
                    to_add_ids = {identifiers[ref]:item}
                    ref += 1
                    sales_dicctionary.update(to_add_ids)
                     
                json.dump(sales_dicctionary, f)
                f.write("\n")  

if __name__ == "__main__":
    create = Creator()
    create.convert_to_dot_json()