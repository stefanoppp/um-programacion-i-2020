persona = {"nombre": None,
           "edad": None,
           "dirección": None,
           "teléfono": None}

for item in persona:
    persona[item] = input("Cual es su " + item + "? ")

print(persona["nombre"] +
      " tiene " +
      persona["edad"] +
      " años, vive en " +
      persona["dirección"] +
      " y su número de teléfono es " +
      persona["teléfono"])
