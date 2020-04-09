
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo
# al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre
# anterior a la M y los hombres con un nombre posterior a la N y el grupo B
# por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
# y muestre por pantalla el grupo que le corresponde.


def interfaz(nombre, gen):

    if not nombre or not gen:
        print("No ingreso los campos obligatorios")

    if ((nombre[0] <= "M" and gen == ("Mujer")) or
       (nombre[0] >= "N" and gen == "Hombre")):

        print("Perteneces al grupo A")

    else:
        print("Perteneces al grupo B")


def main():
    nombre = input("Ingrese su nombre:\n").title()
    gen = input("Ingrese su genero:").title()
    interfaz(nombre, gen)


main()
