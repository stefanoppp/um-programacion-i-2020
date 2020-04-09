class Ten():

    def __init__(self,  day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def std(self):
        if self.month == '01' or self.month == 1:
            self.month = 'Enero'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '02' or self.month == 2:
            self.month = 'Febrero'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '03' or self.month == 3:
            self.month = 'Marzo'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '04' or self.month == 4:
            self.month = 'Abril'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '05' or self.month == 5:
            self.month = 'Mayo'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '06' or self.month == 6:
            self.month = 'Junio'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '07' or self.month == 7:
            self.month = 'Julio'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '08' or self.month == 8:
            self.month = 'Agosto'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '09' or self.month == 9:
            self.month = 'Septiembre'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '10' or self.month == 10:
            self.month = 'Octubre'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '11' or self.month == 11:
            self.month = 'Noviembre'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        elif self.month == '12' or self.month == 12:
            self.month = 'Diciembre'
            return "{} de {} de {}".format(self.day, self.month, self.year)
        else:
            print("Escriba el mes en formato mm")


#dia = int(input("Ingrese el numero del dia: "))
#mes = input("Ingrese el mes en formato mm: ")
#ano = int(input("Ingrese el numero del ano: "))
date = Ten('04', '07', 1776)
#date = Ten(dia, mes, ano)
print(date.std())




