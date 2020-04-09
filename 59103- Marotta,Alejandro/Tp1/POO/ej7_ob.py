
class Frase():

    def __init__(self,frase,letra):

        self.frase = frase.lower() #Para que no importe si esta en minuscula o mayuscula
        self.letra = letra.lower()


    def contar(self):
        self.cantidad = self.frase.count(self.letra)
        
        print("\n")
        print("La letra {} se repite {} veces".format(self.letra,self.cantidad))



def main():
    frase = input("Ingrese una frase y toque enter: \n")
    letra = input("¿Que letra desea saber cuantas veces se repite?\n")

    cantidad = Frase(frase,letra)
    cantidad.contar()

    

if __name__ == "__main__":
    main()