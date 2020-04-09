'''Escribir un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un dic. Después debe mostrar por
pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección>
y su número de teléfono es
<teléfono>.'''


def logica():

    dic = {'Nombre': '', 'Edad': '', 'Direccion': '', 'Telefono': ''}

    for palabra in dic:
        dic[palabra] = input("\nIngrese su "+palabra+":")

    print(dic["Nombre"]+" tiene "+dic["Edad"]+" anos, vive en " +
          dic["Direccion"] + " y su numero de telefono es "+dic["Telefono"])


logica()
