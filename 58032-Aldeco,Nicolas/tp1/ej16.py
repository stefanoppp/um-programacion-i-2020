class Sales():
    def __init__(self):
        self.texto = []
        for i in (open('./ventas.txt', 'r')):
            self.texto.append(i)

    def print_sales(self):
        num = 0
        for venta in self.texto:
            num += 1
            print('Venta numero '+str(num)+':')
            list_venta = venta.split(',')
            sale = []
            for item in list_venta:
                item = item.lstrip(' ')
                sale.append(item)
            sale[1] = float(sale[1])
            print(('Nombre:{c},Monto:{m},Descripcion:{d},Forma de pago:{p}').format(
                c=sale[0],
                m=str(sale[1]),
                d=sale[2],
                p=sale[3]
            ))


if __name__ == "__main__":
    obj = Sales()
    obj.print_sales()
