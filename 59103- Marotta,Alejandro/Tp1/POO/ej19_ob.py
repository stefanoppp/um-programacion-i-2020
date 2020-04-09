""" Ejercicio 19
Crear un programa similar al ejercicio 18 (incluyendo la funcionalidad del ejercicio 17) donde
los datos del archivo de texto serán:
Nombre y apellido, número de tarjeta de crédito, código de verificación, tipo de tajeta de
crédito, monto de la venta, descripción de venta.
Los datos debén manejarse de la siguiente manera:
Crear una clase TarjetaCredito que almacene los datos de: Nombre y apellido, número de
tarjeta de crédito, código de verificación, tipo de tajeta de crédito.
Crear una clase Venta que almacene los datos de: monto de la venta, descripción de venta y
un objeto de la clase TarjetaCredito.
El formato de los datos JSON deberá respetar el formato de Venta con los datos de monto y
descripción y el objeto de la clase Venta. """

import json

class ValorVacio(ValueError):
    def __init__(self):         
        super(ValorVacio, self).__init__()


class TarjetaCredito():

    def __init__(self,nombre = None,num= None,cod = None,tipo= None):

        self.nombre = nombre
        self.numero = num
        self.codigo = cod
        self.tipo = tipo

        self.datos= {}
        self.datos['tarjeta'] = []     

        

    def get_datos(self):
        return self.datos['tarjeta']

    def set_datos(self,nombre,num,cod,tipo):

        self.nombre = nombre
        self.numero = num
        self.codigo = cod
        self.tipo = tipo

        self.datos['tarjeta'] =({
            'nombre': self.nombre,
            'numero de tarejeta': self.numero,
            'codigo de verificacion': self.codigo,
            'tipo de tarjeta': self.tipo})
      


class Venta():

    def __init__(self,filas):

        self.filas = filas

        self.tarjeta = TarjetaCredito()

        self.datos= {}
        self.datos['ventas'] = []

        for valor in self.filas :
            lista = valor.split(",")

            self.tarjeta.set_datos(lista[0],lista[1],lista[2],lista[3])


            self.datos['ventas'].append({
            
            'monto': lista[4],
            'descripcion': lista[5],
            'tarjeta': self.tarjeta.get_datos()})

    def get_ventas(self):
        return self.datos


class General():

    def __init__(self, path):
        
        self.path = path
        self.documento = open(self.path,"r")
        self.texto = self.documento.read()       

        self.filas = self.texto.split("\n")

        self.venta = Venta(self.filas)

        self.datos = self.venta.get_ventas()

    
    
    def pasar_JSON(self):
           
        with open('VENTAS.json', 'w') as file:
            json.dump(self.datos, file, indent=4)

    def mostrar(self):

        with open('VENTAS.json') as file:
            datos = json.load(file)
       

        for venta in datos['ventas']:
            try:
                values = venta.values()
                if "" in values:
                    raise ValorVacio()

                else:
                    print('Monto: $', venta['monto'])
                    print('Descripcion: ', venta['descripcion'])
                    print('Datos Tarjeta: ', venta['tarjeta'])
                    print('')

            except ValorVacio:
                print ("---------ERROR----------")
                print ('Ningun valor puede estar vacio')
                print("\n")


""" Ejemplo:

venta = General("c:/Users/amaro/OneDrive/Documents/Programacion 1/TP1/ventas_tarjeta.txt")

venta.pasar_JSON()

venta.mostrar()

"""

        

    