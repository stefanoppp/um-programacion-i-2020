""" Ejercicio 15
Crear un programa que lea un archivo de texto que va a contener datos de una venta y
mostrarlo por pantalla.
El formato será:
Nombre y apellido, monto de la venta, descripción, forma de pago (contado o tarjeta)
El archivo contendrá una línea por cada venta, y podrá contener múltiples ventas.
 """

class Ventas():
   
    def __init__(self, path):
        
        self.path = path
        self.documento = open(self.path,"r")
        self.texto = self.documento.read()      
         

        self.filas = self.texto.split("\n")    
                        
        
       

    def mostrar(self):

        for valor in self.filas :
            print("* ",valor)


#Al ser para cualquier archivo le coloco esta pequeña "Interfaz"
    
def main():

    p = input("Ingrese el path del archivo de ventas: \n ")

    p = p.strip()
    
    venta = Ventas(p)

    print("\n")

    venta.mostrar()


if __name__ == "__main__":
    main()


