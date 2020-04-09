from ej_9 import Datos


class Interfaz():
    def interfaz(self):
        x = Datos()
        nombre = str(input("Ingrese su nombre:\n"))
        edad = int(input("Ingrese su edad:\n"))
        direccion = input("Ingrese la direccion de su domicilio:\n")
        telefono = int(input("Ingrese su numero telefonico:\n"))
        x.set_name(nombre)
        x.set_age(edad)
        x.set_direction(direccion)
        x.set_number(telefono)
        name = x.get_name()
        age = x.get_age()
        direction = x.get_direction()
        tel = x.get_number()
        x.set_dic(x.asignacion(name, age, direction, tel))
        dic = x.get_dic()
        print(str(dic[nombre]) + " tiene " + str(dic[edad]) + " años, vive en "
              + str(dic[direccion]) + " y su numero de telefono es "
              + str(dic[telefono]))


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
