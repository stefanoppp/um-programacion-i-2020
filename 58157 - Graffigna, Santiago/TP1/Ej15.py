
class Sales_Department():

    def __init__(self):

        self.file = []

        for x in (open('sales.txt', 'r')):
            self.file.append(x)

    def sales_info(self):

        print("")
        for line in self.file:
            print(line, end = "")
        print("\n")

if __name__ == "__main__":
    department = Sales_Department()
    department.sales_info()