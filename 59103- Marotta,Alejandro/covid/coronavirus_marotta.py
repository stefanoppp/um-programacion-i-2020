import requests

URL = 'https://corona-stats.online/'
page = requests.get(URL)

texto = page.text

cuadro = page.text[texto.find("╔"):texto.find("╝")+1]

lista = cuadro.split("║")


datos = []

for valor in range (len(lista)):
    if valor % 2 == 1 :
        datos.append(lista[valor])
    else:
        pass

diccionario = {}

for x in datos:
    pais_crudo= x[x.find("│")+1:x.find("(")]
    pais_listo = pais_crudo.strip()

    diccionario[pais_listo] = x

diccionario["World"] = datos[1]
    
def buscar_pais(pais):
    print(datos[0])
    print(diccionario[pais])

i = 0
while i == 0:
    pais = input("Ingrese el nombre de un pais para buscar sus estadisticas de coronavirus: ")
    buscar_pais(pais)
    
    print("\n")

    i = int(input("Si desea continuar ingrece 0 , de lo contrario 1: "))
    print("\n")





