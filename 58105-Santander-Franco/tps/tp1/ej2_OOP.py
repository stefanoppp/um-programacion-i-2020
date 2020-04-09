class Pizza():

    def __init__(self):
        self.pizza = ""
        self.ingre = ""

    def set_pizza(self, pizza):
        self.pizza = pizza

    def get_pizza(self):
        return self.pizza

    def set_ingre(self, ingre):
        self.ingre = ingre

    def get_ingre(self):
        return self.ingre


class Flavours():
    def full_pizza(self, pizza, ingre):
        if pizza == "s":
            if ingre == "p":
                return ("Usted ordeno una pizza vegetariana la cual"
                        " tiene salsa de tomate, queso mozzarella y "
                        "pimientos")
            else:
                return("Usted ordeno una pizza vegetariana la cual"
                       "tiene salsa de tomate, queso mozzarella y "
                       "tofu")
        else:
            if ingre == "p":
                return("Usted ordeno una pizza no vegetariana la cual tiene"
                       " salsa de tomate, queso mozzarella y peperoni")
            elif ingre == "j":
                return("Usted ordeno una pizza no vegetariana la cual tiene"
                       " salsa de tomate, queso mozzarella y jamon")
            else:
                return("Usted ordeno una pizza no vegetariana la cual tiene"
                       " salsa de tomate, queso mozzarella y salmon")

    def val_pizza_veggie(self, pizza, ingre):
        if pizza == "s" or pizza == "n":
            if pizza == "s":
                if ingre == "p" or ingre == "t":
                    return True
                else:
                    print("Ingrese una variante valida")
                    return False
            else:
                if ingre == "p" or ingre == "j" or ingre == "s":
                    return True
                else:
                    print("Ingrese una variante valida")
                    return False
        print("Ingrese una variante valida")
        return False

    def select_flavour(self, pizza):
        if pizza == "s":
            ingre = str(input("¿Que ingredientes desea en su pizza?\n"
                              "Ingrese:\np -> Para añadir pimientos a"
                              "su pizza\nt -> Para añadir tofu a su"
                              "pizza\n"))
            return(ingre)
        else:
            ingre = ingre = str(input("¿Que ingredientes desea en su pizza?\n"
                                      "Ingrese:\np -> Para añadir peperomi a"
                                      "su pizza\nj -> Para añadir jamon a su "
                                      "pizza\ns -> Para añadir salmon a su"
                                      "pizza\n"))
            return(ingre)


if __name__ == "__main__":
    hola = Pizza()
