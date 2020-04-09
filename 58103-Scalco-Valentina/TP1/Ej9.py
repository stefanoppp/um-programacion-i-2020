nombre = input("Ingrese su nombre\n")
edad = input("Ingrese su edad\n")
direccion = input("Ingrese su direccion\n")
telefono = input("Ingrese su telefono\n")
info = {"Nombre": nombre, "Edad": edad, "Direccion": direccion,"Telefono": telefono}
print(info["Nombre"], "tiene", info["Edad"], "años, vive en",
info['Direccion'], "y su telefono es", info['Telefono'])
