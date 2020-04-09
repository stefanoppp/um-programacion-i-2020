'''Escribir un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un self.dic. Después debe mostrar por
pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección>
y su número de teléfono es
<teléfono>.'''


class Datos():

    def __init__(self):

        self.dic = {'Nombre': '', 'Edad': '', 'Direccion': '', 'Telefono': ''}

    def ingreso(self):

        for palabra in self.dic:
            self.dic[palabra] = input("\nIngrese su "+palabra+":")
        return(self.dic)

    def pantalla(self, dic):
        print(dic["Nombre"]+" tiene "+dic["Edad"]+" anos, vive en " +
              dic["Direccion"] + " y su numero de telefono es " +
              dic["Telefono"])


if __name__ == "__main__":
    D = Datos()
    x = D.ingreso()
    D.pantalla(x)
