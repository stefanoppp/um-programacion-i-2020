fecha = input("Ingrese una fecha en formato dd/mm/aaaa\n")
fecha = fecha.split("/")
mes = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio',
8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
print("La fecha introducida es:", fecha[0], "de", mes[int(fecha[1])], "de", fecha[2])