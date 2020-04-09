""" Ejercicio 8 
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura, y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> es cada 
una des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario.  """

asignatura = ["Matemáticas", "Física","Química","Historia","Lengua"]


def imprimir(diccionario):
    for clave, valor in diccionario.items(): 
        print ("En la asignatura %s has sacado %s" % (clave, valor))
    


def asignar():
    dic= {}
    for x in asignatura:
        nota = input("Ingrese la nota obtenida en {} ".format(x))
        dic[x] = nota
    print("\n")
    return dic


def start():
    imprimir(asignar())


start()