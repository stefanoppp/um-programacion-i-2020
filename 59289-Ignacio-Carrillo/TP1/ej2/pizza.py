from tipo import Tipo

class Pizza():

    def __init__(self):
        self.tipo="" #Vegetariana o no vegetariana

    def setTipo(self):
        while True:
            try:
                self.tipo = input("\nTipo de pizza deseada -- V(Vegetariana) / NV(No Vegetariana): ")
                self.tipo = self.tipo.upper()
                if self.tipo == "NV":
                    self.tipo = "No Vegetariana"
                    break
                elif self.tipo == "V":
                    self.tipo = "Vegetariana"
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\nTipo de pizza invalido, intente nuevamente")

    def getTipo(self):
        return self.tipo
