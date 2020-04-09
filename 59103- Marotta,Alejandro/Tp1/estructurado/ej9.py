""" Ejercicio 9 
Escribir un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
vive en <dirección> y su número de teléfono es <teléfono>.  """


def guardar(nombre,edad,direc,tel):

    dic = {"nombre":nombre,"edad":edad,"direccion":direc,"telefono":tel }    
    return dic

def imprimir(diccionario):

    dic = diccionario    

    print("{} tiene {} años, vive en {} y su numero de telefono es {}".format(dic["nombre"],dic["edad"],dic["direccion"],dic["telefono"]))

def start():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    direc = input("Ingrese su direccion: ")
    telefono = input("Ingrese su telefono: ")

    imprimir(guardar(nombre,edad,direc,telefono))

start()



