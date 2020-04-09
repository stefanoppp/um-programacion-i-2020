from os import system
 
name = input("Ingrese su nombre: ").title()
age = int(input("Ingrese su edad: "))
address = input("Ingrese su direccion: ").title()
tel_number = int(input("Ingrese su telefono: "))
system('clear')

diccionary = {
  "nombre": name,
  "edad": age,
  "direccion": address,
  "telefono": tel_number
}
print(diccionary["nombre"], "tiene", diccionary["edad"], "años, vive en", diccionary["direccion"], "y su telefono es", diccionary["telefono"])

