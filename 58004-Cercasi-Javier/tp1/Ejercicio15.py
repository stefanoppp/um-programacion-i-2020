'''Crear un programa que lea un archivo de lista que va a contener datos
de una venta y mostrarlo por pantalla. El formato será:
Nombre y apellido, monto de la venta, descripción, forma de pago
(contado o tarjeta). El archivo contendrá una línea por cada venta,
y podrá contener múltiples ventas.'''


def interfaz(nombre):
    lista = []

    datos = (open("/home/javi/Programacion_1/um-programacion-i-2020/" +
                  "58004-Cercasi-Javier/tp1/Ejercicio15.txt", "r"))

    texto = datos.read().replace("\n", ",")
    # texto=texto.replace(",","")
    lista = list(texto.strip().split(","))
    try:
        ubi = lista.index(nombre)
        print("\nSus datos son:\n")
        print("Nombre:", lista[ubi], "\nMonto de la venta:", lista[ubi+1])
        print("Descripcion:", lista[ubi+2], "\nForma de pago:", lista[ubi+3])

    except:
        print("\nSu nombre no esta en la lista.\n")
        pass


def main():
    nombre = input("Ingrese el nombre y apellido para obtener sus" +
                   " datos:\n").title()
    interfaz(nombre)


main()
