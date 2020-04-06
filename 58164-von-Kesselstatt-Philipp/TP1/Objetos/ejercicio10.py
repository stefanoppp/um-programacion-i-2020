class fecha():
    def cambioFormato(self, fecha):

        fecha = fecha.split("/")

        self.año = ['enero',
                    'febrero',
                    'marzo',
                    'abril',
                    'mayo',
                    'junio',
                    'julio',
                    'agosto',
                    'septiembre',
                    'octubre',
                    'noviembre',
                    'diciembre']

        self.fechaFormato = (fecha[0] +
                             " de " +
                             self.año[int(fecha[1])-1] +
                             " del " +
                             fecha[2]
                             )

        return self.fechaFormato


"""
ejercicio10 = fecha()
fecha = input("ingrese la fecha en formato dd/mm/aaaa ")
print(ejercicio10.cambioFormato(fecha))
"""
