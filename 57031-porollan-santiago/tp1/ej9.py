if __name__ == "__main__":
    persona = {}
    persona["nombre"] = input("nombre: ")
    persona["edad"] = input("edad: ")
    persona["direccion"] = input("direccion: ")
    persona["telefono"] = input("telefono: ")
    print(persona["nombre"], " vive en ", persona["direccion"], " tiene ", 
          persona["edad"], " años y su tel es ", persona["telefono"])