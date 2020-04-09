from ej2_OOP import Pizza, Flavours


class Interfaz():
    def interfaz(self):
        menu = Pizza()
        gustos = Flavours()
        pizza = str(input("¿Que desea pedir?\nIngrese :\ns -> Para pizza "
                          "vegetariana\nn -> Para pizza no vegetariana\n"))
        menu.set_pizza(pizza)
        zappi = menu.get_pizza()
        ingre = gustos.select_flavour(zappi)
        menu.set_ingre(ingre)
        ingrediente = menu.get_ingre()
        verificador = gustos.val_pizza_veggie(zappi, ingrediente)
        if verificador is True:
            print(gustos.full_pizza(zappi, ingrediente))
        else:
            print("Error")


if __name__ == "__main__":
    Interfaz = Interfaz()
    Interfaz.interfaz()
