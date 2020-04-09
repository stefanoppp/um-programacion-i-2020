""" Ejercicio 18
Modificar el programa del ejercicio 17 agregando un control de datos vacíos.
Si por algún motivo alguno de los datos viene vacío o igual a "" debemos generar una
excepción indicando que ocurrió un problema con la fuente de datos y notificar por pantalla.
La excepción debe ser una excepción propia.


"""
import json

class ValorVacio(ValueError):
    def __init__(self):         
        super(ValorVacio, self).__init__()

class Ventas():
   
    def __init__(self, path):
        
        self.path = path
        self.documento = open(self.path,"r")
        self.texto = self.documento.read()       

        self.filas = self.texto.split("\n")     
  
                      
    def pasar_JSON(self):

        self.datos= {}
        self.datos['ventas'] = []

        for valor in self.filas :
            lista = valor.split(",")

            self.datos['ventas'].append({
            'nombre': lista[0],
            'monto': lista[1],
            'descripcion': lista[2],
            'formapago': lista[3]})
        
        with open('ARCHIVO_ORIGINAL.json', 'w') as file:
            json.dump(self.datos, file, indent=4)


    def mostrar(self):

        with open('ARCHIVO_ORIGINAL.json') as file:
            datos = json.load(file)

        
        

        for venta in datos['ventas']:
            try:
                values = venta.values()
                if "" in values:
                    raise ValorVacio()

                else:
                    print('Nombre: ', venta['nombre'])
                    print('Monto: $', venta['monto'])
                    print('Descripcion: ', venta['descripcion'])
                    print('Forma de pago: ', venta['formapago'])
                    print('')

            except ValorVacio:
                print ("---------ERROR----------")
                print("Error en los datos del cliente: ", venta['nombre'])
                print ('Ningun valor puede estar vacio')
                print("\n")


""" Ejemplo:

venta = Ventas("c:/Users/amaro/OneDrive/Documents/Programacion 1/TP1/datos_ventas.txt")

venta.pasar_JSON()
venta.mostrar()

"""
            