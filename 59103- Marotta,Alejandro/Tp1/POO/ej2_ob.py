

class Pizza():

    def __init__(self,tipo):

        self.ingredientes = ["Mozzarella","Tomate"]
        self.tipo = tipo

    def seleccion(self):
        pass

    def agregar(self,agregado):
        self.agregado = agregado
        self.ingredientes.append(self.agregado)

    def mostrar(self):

        self.ing = str(self.ingredientes).replace("[","")
        self.ing = self.ing.replace("]","")
        self.ing = self.ing.replace("'","")


        print("La pizza es ", self.tipo," y sus ingredientes son ", self.ing)


class Vegetariana(Pizza):

    def seleccion(self):
        ing = int(input("Seleccione uno de los siguientes ingredientes: \n 1-Pimiento \n 2-Tofu \n"))
        if ing == 1:
            i = "Pimiento"
        if ing == 2:
            i = "Tofu"
        self.agregar(i)




class Clasica(Pizza):

    def seleccion(self):
        ing = int(input("Seleccione uno de los siguientes ingredientes: \n 1-Peperoni \n 2-Jamon \n 3-Salmon \n"))
        
        if ing == 1:
            i = "Peperoni"
        if ing == 2:
            i = "Jamon"
        if ing == 3:
            i = "Salmon"
        
        self.agregar(i)


        


def main():
    selec = input("Seleecione el tipo de pizza \n 1-Vegetariana \n 2-Clasica \n")

    if selec == "1":

       pizza = Vegetariana("Vegetariana")
       pizza.seleccion()
       pizza.mostrar()

    elif selec == "2":

       pizza = Clasica("Clasica")
       pizza.seleccion()
       pizza.mostrar()
    
    else:
        print("Opcion no valida")

if __name__ == "__main__":
    main()
   
   
   
   
