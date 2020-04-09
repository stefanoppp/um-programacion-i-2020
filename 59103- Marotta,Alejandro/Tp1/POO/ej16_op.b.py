""" Ejercicio 16
Modificar el ejercicio 15 y hacer que los datos se muestren con una etiqueta por delante """

class Ventas():
   
    def __init__(self, path):
        
        self.path = path
        self.documento = open(self.path,"r")
        self.texto = self.documento.read()      
  

        self.ventas = {}

        self.filas = self.texto.split("\n")

        for valor in self.filas :
                        
            nombre = valor[0:valor.find(",")].strip()

            self.ventas[nombre] = valor    

        

    def mostrar(self,nombre):

        datos = self.ventas[nombre].split(",")


        print("Nombre: " , datos[0])
        print("Monto: $" , datos[1])
        print("Descripcion: " , datos[2])
        print("Forma de pago: " , datos[3])


#Al ser para cualquier archivo le coloco esta pequeña "Interfaz"
    
def main():

    p = input("Ingrese el path del archivo de ventas: \n ")

    p = p.strip()
    
    venta = Ventas(p)

    n = input("Ingrese el nombre del cliente: \n")

    n = n.strip()

    print("\n")

    venta.mostrar(n)


if __name__ == "__main__":
    main()