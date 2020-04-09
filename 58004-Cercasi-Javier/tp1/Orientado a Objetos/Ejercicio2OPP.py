'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a
sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
* Ingredientes vegetarianos: Pimiento y tofu.
* Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana
o no, y en función de su respuesta le muestre un menú con los ingredientes
disponibles para que elija. Solo se puede eligir un ingrediente además de la
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar
por pantalla si la pizza elegida es vegetariana o no y todos los
ingredientes que lleva.'''


class Pizza():

    def __init__(self):
        self.tipo = ''

    def ingreso(self):

        self.tipo = input('''Que pizza desea?Vegetariana/Comun\n''').title()
        print("\nIngrese un ingrediente de los de la lista:\n")
        return(self.tipo)

    def ingredientes(self):

        if not self.tipo:
            print("\nNo ingreso los campos obligatorios")

        if self.tipo == "Vegetariana":
            print("-Pimiento\n-Tofu\n")

        elif self.tipo == "Comun":
            print("\n-Peperoni\n-Jamón\n-Salmón")

        else:
            print("Vuelva a intentarlo")

        return(input())

    def pantalla(self):
        print("\nSe Preparara pizza "+self.ingreso(),
              " con ", self.ingredientes())


if __name__ == "__main__":
    P = Pizza()
    P.pantalla()
