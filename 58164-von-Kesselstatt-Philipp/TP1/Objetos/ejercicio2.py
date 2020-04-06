class Pizza():
    def __init__(self, ingrediente=None):
        self.ingrediente = ingrediente
        self.ingredientesV = ["Pimiento", "Tofu"]
        self.ingredientesNV = ["Peperoni", "Jamón", "Salmón"]

    def getIngrediente(self):
        return self.ingrediente

    def setIngrediente(self, ingrediente):
        self.ingrediente = ingrediente

    def esVegetariana(self):
        if self.ingrediente in self.ingredientesV:
            return True
        else:
            return False

    def getIngredientesV(self):
        return self.ingredientesV

    def getIngredientesNV(self):
        return self.ingredientesNV


class Interfaz():

    def __init__(self):
        self.pizza = Pizza()

    def preguntarV(self):
        inputV = input("quere una pizza vegetariana? s/n ")
        while inputV != "s" and inputV != "n":
            if inputV == "s":
                return True
            elif inputV == "n":
                return False
            else:
                input("quere una pizza vegetariana? ingrese s o n ")

    def preguntarIngrediente(self):
        if self.preguntarV():
            self.ingredientes = self.pizza.getIngredientesV()
        else:
            self.ingredientes = self.pizza.getIngredientesNV()

        print("\nEliga un ingrediente: ")
        for item in self.ingredientes:
            print(item, item[0])

        self.choices = [item[0].lower() for item in self.ingredientes]
        self.choice = ""

        while (self.choice not in self.choices):

            self.choice = input("\nElija la inicial del ingrediente  ").lower()

        self.pizza.setIngrediente(self.ingredientes[self.choices.index(self.choice)])

    def imprimirPizza(self):

        self.vegStatement = " es vegetariana y" if self.pizza.esVegetariana() else ""

        print("\nSu pizza" + self.vegStatement + " lleva los siguentes ingredientes:")
        print("Muzzarella")
        print("Tomate")
        print(self.pizza.getIngrediente())


"""
ejercicio2 = Interfaz()
ejercicio2.preguntarIngrediente()
ejercicio2.imprimirPizza()
"""
