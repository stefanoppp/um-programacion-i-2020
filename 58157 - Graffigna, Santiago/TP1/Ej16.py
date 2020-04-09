class Sales_Department():

    def __init__(self):

        self.file = []

        for x in (open('sales.txt', 'r')):
            self.file.append(x)

    def sales_info(self):
        print("")
        for line in self.file:
            lineas = line.split(',')
            print("Nombre: " + lineas[0] + ", " +  "Monto:" + lineas[1] + ", " + "Descripcion:" + lineas[2] + ", " + "Forma de pago:" + lineas[3])
        print("\n")

if __name__ == "__main__":
    department = Sales_Department()
    department.sales_info()