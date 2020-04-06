

class Menu():
    def __init__(self):
        self.tipo = "No veg"
        self.ingredientes = ["pimiento", "tofu","peperoni", "jamon", "salmon"]
    
    def seleccionar_ingredientes(self):
        ingredientes = []
        for ingrediente in self.ingredientes:
            cond = input("Agregar " + ingrediente + "? si no: ")
            if cond == "si":
                ingredientes.append(ingrediente)
        return ingredientes


class MenuVegetariano(Menu):
    def __init__(self):
        self.tipo = "Veg"
        self.ingredientes = ["pimiento", "tofu"]


class Pizza():
    def __init__(self, ingredientes=[], tipo=""):
        self.ingredientes = ["tomate", "mozzarella"] + ingredientes
        self.tipo = tipo
    
    def show_pizza(self):
        print("pizza ", self.tipo)
        print("ingredientes: ", " ".join(self.ingredientes))


if __name__ == "__main__":
    # preguntar si es vegetariana
    es_vegetariana = input("pizza vegetariana? si, no: ")
    menu = MenuVegetariano() if es_vegetariana == "si" else Menu()
    pizza = Pizza(menu.seleccionar_ingredientes(), menu.tipo)
    pizza.show_pizza()
