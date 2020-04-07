class Tipo():

    def __init__(self):
        self.ingredientes=[]
        self.ingredientes.append("Mozzarella")
        self.ingredientes.append("Tomate")

    def setIngredientes(self,tipo):
        if tipo=='No Vegetariana':
            while True:
                try:
                    eleccion=int(input("""
1-Peperoni                    
2-Jamon                   
3-Salmon\n                    
Elija su ingrediente: """))
                    if(eleccion==1):
                        self.ingredientes.append("Peperoni")
                        break
                    elif(eleccion==2):
                        self.ingredientes.append("Jamon")
                        break
                    elif(eleccion==3):
                        self.ingredientes.append("Salmon")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("\nIntroduzca una opcion valida")
        else:
             while True:
                try:
                    eleccion = int(input("""
1-Pimiento                    
2-Tofu\n                    
Elija su ingrediente: """))
                    if(eleccion==1):
                        self.ingredientes.append("Pimiento")
                        break
                    elif(eleccion==2):
                        self.ingredientes.append("Tofu")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("\nIntroduzca una opcion valida")

    def getIngredientes(self):
        return self.ingredientes
