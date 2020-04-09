"""Modificar el ejercicio 15 y hacer que los datos se muestren con una
etiqueta por delante, algo así como: Nombre: xxxxxxxxx, monto: xxxx.xx,
descripción: xxxxxxxxxx, forma de pago: xxxxxxxx."""


def interfaz(nombre):
    lista = []

    datos = (open("/home/javi/Programacion_1/um-programacion-i-2020/" +
                  "58004-Cercasi-Javier/tp1/Ejercicio15.txt", "r"))

    texto = datos.read().replace("\n", ",")
    lista = list(texto.strip().split(","))

    try:
        ubi = lista.index(nombre)
        print("\nSus datos son:\n\nNombre:", str((len(lista[ubi]))*"x"),
              "\nMonto de la venta:", str(((len(lista[ubi+1]))-1)*"x"),
              "\nDescripcion:", str(((len(lista[ubi+2]))-1)*"x"),
              "\nForma de pago:", str(((len(lista[ubi+3]))-1)*"x"))

    except:
        print("\nSu nombre no esta en la lista.\n")
        pass


def main():
    nombre = input("Ingrese el nombre y apellido para obtener sus" +
                   " datos:\n").title()
    interfaz(nombre)


main()
