class Date():
    def __init__(self, fecha):
        self.values = fecha.split('/')
        self.meses = ['Enero', 'Febrero', 'Marzo', 'Abril',
                      'Mayo', 'Junio', 'Julio', 'Agosto',
                      'Septiembre', 'Octubre', 'Noviembre',
                      'Diciembre']

    def get_date(self):
        for mm in range(12):
            if ((int(self.values[1])-1) == mm):
                mes = self.meses[mm]
        return('{d} de {m} de {a}').format(
            d=self.values[0], m=mes, a=self.values[2])


if __name__ == '__main__':
    fecha = input('dd/mm/aaaa = ')
    obj = Date(fecha)
    print(obj.get_date())
