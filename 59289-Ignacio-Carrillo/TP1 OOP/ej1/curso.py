class Curso():
    def __init__(self):
        pass

    def getRespuesta(self,nombre,sexo):        #Generar respuesta
        if sexo=='F' and ord(nombre[0])<=77 and ord(nombre[0])>64:
            print("\nLa alumna {} pertenece al grupo A" .format(nombre))
        elif sexo=='F' and ord(nombre[0])<=90 and ord(nombre[0])>77:
            print("\nLa alumna {} pertenece al grupo B" .format(nombre))
        elif sexo=='M' and ord(nombre[0])<=77 and ord(nombre[0])>64:
            print("\nEl alumno {} pertenece al grupo B" .format(nombre))
        elif sexo=='M' and ord(nombre[0])<=90 and ord(nombre[0])>77:
            print("\nEl alumno {} pertenece al grupo A" .format(nombre))
        else:
            print("\n***ERROR--El nombre introducido es invalido***") #excepcion nombre
        print()

