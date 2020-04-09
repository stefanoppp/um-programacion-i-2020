""" Ejercicio 11
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un
curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre
por pantalla los créditos de cada asignatura en el formato <asignatura> tiene
<créditos> créditos, donde <asignatura> es cada una de las asignaturas del
curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de
créditos del curso """

asignaturas = {}

def almacenar(key,value):
    asignaturas [key] = int(value)

def imprimir():
    for key in asignaturas:
        print(key, " tiene ", asignaturas[key], " creditos. \n")

def creditos():
    total = 0
    for key in asignaturas:
        total = total + asignaturas[key]
    print ("El curso tiene {} creditos".format(total))

    

def pedir():
    nombre = input("Ingrese la asignatura: ")
    cred = input("Ingrese los creditos: ")
    almacenar(nombre,cred)


def start():
    seguir = True
    
    while seguir == True:
        pedir()

        a = input("Desea seguir agregando asignaturas S/N : ")
        
        if a == "N":
            seguir = False

    print("\n")

    imprimir()
    creditos()

start()        

    

    
            



    


    

