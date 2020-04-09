pizza = str(input("¿Que desea pedir?\nIngrese :\ns -> Para pizza "
                  "vegetariana\nn -> Para pizza no vegetariana\n"))
if pizza == "s" or pizza == "n":
    if pizza == "s":
        ingre = str(input("¿Que ingredientes desea en su pizza?\nIngrese:\n"
                          "p -> Para añadir pimientos a su pizza\nt -> Para"
                          "añadir tofu a su pizza\n"))
        if ingre == "p" or ingre == "t":
            if ingre == "p":
                print("Usted ordeno una pizza vegetariana la cual tiene "
                      "salsa de tomate, queso mozzarella y pimientos")
            else:
                print("Usted ordeno una pizza vegetariana la cual tiene"
                      "salsa de tomate, queso mozzarella y tofu")
        else:
            print("Ingrese una letra valida")
    else:
        ingre = str(input("¿Que ingredientes desea en su pizza?\n"
                          "Ingrese:\np -> Para añadir peperomi a"
                          "su pizza\nj -> Para añadir jamon a su "
                          "pizza\ns -> Para añadir salmon a su pizza\n"))
        if ingre == "p" or ingre == "j" or ingre == "s":
            if ingre == "p":
                print("Usted ordeno una pizza no vegetariana la cual tiene"
                      "salsa de tomate, queso mozzarella y peperoni")
            elif ingre == "j":
                print("Usted ordeno una pizza no vegetariana la cual tiene"
                      "salsa de tomate, queso mozzarella y jamon")
            else:
                print("Usted ordeno una pizza no vegetariana la cual tiene"
                      "salsa de tomate, queso mozzarella y salmon")
        else:
            print("Ingrese una letra valida")
else:
    print("Ingrese una letra valida")
