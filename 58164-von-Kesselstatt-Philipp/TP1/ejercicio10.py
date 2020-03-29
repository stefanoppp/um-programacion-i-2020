def ejercicio10(fecha):

    fecha = fecha.split("/")

    año = ['enero',
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

    return fecha[0] + " de " + año[int(fecha[1])-1] + " del " + fecha[2]


print(ejercicio10(input("ingrese la fecha en formato dd/mm/aaaa ")))
