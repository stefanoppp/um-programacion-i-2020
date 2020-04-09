class Fecha():
    def __init__(self):
        self.date = ''

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def meses(self):
        self.months = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
                       5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
                       9: 'septiembre', 10: 'octubre', 11: 'noviembre',
                       12: 'diciembre'}
        return self.months

    def fecha(self, date):
        self.fecha = []
        self.fecha.append(date[0:2])
        self.fecha.append(date[3:5])
        self.fecha.append(date[6:10])
        return self.fecha


if __name__ == "__main__":
    hola = Fecha()
