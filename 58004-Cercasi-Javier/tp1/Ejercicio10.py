'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde
<mes> es el nombre del mes.'''


def logica():

    Meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO",
             "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]

    res = input("Dime la fecha en formato dd/mm/aaaa:\n").split('/')

    print(res[0]+" de "+Meses[int(res[1])-1]+" de "+res[2])


logica()
