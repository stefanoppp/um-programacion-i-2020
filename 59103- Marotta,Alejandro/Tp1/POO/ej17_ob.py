"""
Ejercicio 17
Crear un programa que lea el archivo del ejercicio 15 y lo convierta a formato JSON con el
siguiente formato:
{"nombre":"xxxxxxxxx",''monto":xxxx.xx, "descripcion":"xxxxxxxx", "formapago":"xxxx"}
Debemos mostrarlo por pantalla y crear un archivo llamado ARCHIVO_ORIGINAL.json
donde guardaremos los objetos JSON convertidos
El nombre ARCHIVO_ORIGINAL debe ser el que se definió para el archivo de datos.

"""

import json


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
            print('Nombre: ', venta['nombre'])
            print('Monto: $', venta['monto'])
            print('Descripcion: ', venta['descripcion'])
            print('Forma de pago: ', venta['formapago'])
            print('')


""" Ejemplo:

venta = Ventas("c:/Users/amaro/OneDrive/Documents/Programacion 1/TP1/datos_ventas.txt")

venta.pasar_JSON()
venta.mostrar()

"""

