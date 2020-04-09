from usuario import Usuario
import os

class App():

    def __init__(self):
        pass

    def ejecutar (self):
        obj=Usuario() #creo objeto
        dic={} #creo diccionario
        obj.setNombre()
        obj.setEdad()
        obj.setDireccion()
        obj.setTelefono()
        dic['Nombre']=obj.getNombre()
        dic['Edad']=obj.getEdad()
        dic['Direccion']=obj.getDireccion()
        dic['Telefono']=obj.getTelefono()
        self.imprimir(dic)


    def imprimir (self,diccionario):
        os.system("clear clc")
        print("\n{} tiene {} años, vive en {} y su numero de telefono es {}"
        .format(diccionario['Nombre'],diccionario['Edad'],diccionario['Direccion'],diccionario['Telefono']))
        print()

if __name__ == "__main__":
    app=App()
    app.ejecutar()
    