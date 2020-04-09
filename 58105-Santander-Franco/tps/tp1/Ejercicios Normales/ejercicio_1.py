def main():
    sexo = str(input("Ingrese:\nm -> Para masculino\nf -> Para femenino\n"))
    nombre = str(input("Ingrese su nombre:\n"))
    if sexo == "m":
        if nombre[0] <= "n":
            print("Pertenece al curso B")
        else:
            print("Pertenece al curso A")
    else:
        if nombre[0] <= "l":
            print("Pertenece al curso A")
        else:
            print("Pertenece al curso B")


if __name__ == '__main__':
    main()
