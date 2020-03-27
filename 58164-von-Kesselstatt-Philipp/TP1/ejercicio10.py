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

fecha = input("ingrese la fecha en formato dd/mm/aaaa  ").split("/")

print(fecha[0] + " de " + año[int(fecha[1])-1] + " del " + fecha[2])
