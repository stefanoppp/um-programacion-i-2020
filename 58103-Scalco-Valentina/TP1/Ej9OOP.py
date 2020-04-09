class Personal_info:
    def informacion(self, nombre, edad, direccion, telefono):
        info = {"Nombre": nombre, "Edad": edad, "Direccion": direccion,"Telefono": telefono}
        return(info["Nombre"], "tiene", info["Edad"], "años, vive en",
        info['Direccion'], "y su telefono es", info['Telefono'])
                

def main():
    nombre = input("Ingrese su nombre\n")
    edad = input("Ingrese su edad\n")
    direccion = input("Ingrese su direccion\n")
    telefono = input("Ingrese su telefono\n")
    obj = Personal_info()
    print(obj.informacion(nombre, edad, direccion, telefono))

if __name__ == "__main__":
    main()
