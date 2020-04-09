class Alumno:
    def separate(self, name, sex):
        alfa1 = "AaBbCcDdEeFfGgHhIiJjKkLl"
        alfa2 = "OoPpQqRrSsTtUuVvWwXxYyZz"
        if sex == "m":
            if name in alfa1:
                return("Usted pertenece al Grupo A")
            else:
                return("Usted pertenece al Grupo B")    
        else:
            if name in alfa2:
                return("Usted pertenece al Grupo A")
            else:
                return("Usted pertenece al Grupo B")

def main():
    name = input("Ingrese su nombre \n")
    sex = input("Ingrese si es mujer o si es hombre \n").lower()
    name = name[0]
    sex = sex[0]

    info = Alumno()
    print(info.separate(name, sex))

if __name__ == "__main__":
    main()
