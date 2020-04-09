class Datos():

    def __init__(self):
        self.diccionario = {}
        self.name = ''
        self.age = 0
        self.direction = ''
        self.number = 0

    def set_dic(self, diccionario):
        self.diccionario = diccionario

    def get_dic(self):
        return self.diccionario

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def asignacion(self, nombre, edad, direccion, telefono):
        dic = {}
        dic[nombre] = nombre
        dic[edad] = edad
        dic[direccion] = direccion
        dic[telefono] = telefono
        return dic


if __name__ == "__main__":
    hola = Datos()
