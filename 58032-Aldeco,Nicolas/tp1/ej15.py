class Sales():
    def __init__(self):
        self.texto = []
        for i in (open('./ventas.txt', 'r')):
            self.texto.append(i)

    def print_sales(self):
        num = 0
        for venta in self.texto:
            num += 1
            print('\nVenta numero '+str(num)+':')
            list_venta = venta.split(',')
            sale = []
            for item in list_venta:
                item = item.lstrip(' ')
                item = item.replace('\n', '')
                sale.append(item)
            print(sale)


if __name__ == "__main__":
    obj = Sales()
    obj.print_sales()
