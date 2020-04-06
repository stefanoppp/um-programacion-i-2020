class Persona():
    def __init__(self, nombre, edad, direccion, telefono):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.diccionario = {
                            "nombre": nombre,
                            "edad": edad,
                            "dirección": direccion,
                            "teléfono": telefono
                            }

    def getDiccionario(self):
        return self.diccionario


"""
ejercicio9 = Persona(
                     input("Cual es su nombre? "),
                     input("Cual es su edad? "),
                     input("Cual es su direccion? "),
                     input("Cual es su telefono? "),
                    )


print(ejercicio9.getDiccionario()["nombre"] +
      " tiene " +
      ejercicio9.getDiccionario()["edad"] +
      " años, vive en " +
      ejercicio9.getDiccionario()["dirección"] +
      " y su número de teléfono es " +
      ejercicio9.getDiccionario()["teléfono"])
"""