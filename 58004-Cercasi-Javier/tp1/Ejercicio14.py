'''Crear una variable con triple comillas que contenga un t copiado de algún
lugar de al menos 20 líneas y hacer un conteo de a palabras, al finalizar
el conteo mostrar las 20 palabras que mas se repiten. Mostrar todas las
palabras en orden alfabético y la cantidad que se repite.'''
import operator


def ejercicio(t):

    d = {}
    t = t.replace("(", "")
    t = t.replace(")", "")
    t = t.replace(",", "")
    t = t.replace(".", "")
    t = t.replace("\n", " ")

    for palabra in t.split(" "):
        d[palabra] = t.count(palabra)           #Coloca todas los valores junto a su elemento

    orden = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    orden_alfa = sorted(d.items(), key=operator.itemgetter(0))  #(1) orden por numeros,(0) por letras

    print("\nLas 20 palabras mas repetidas:\n")
    for i in range(1, 20):
        print(orden[i][0], ": ", orden[i][1])

    print("\n\nLas palabras con su frecuencia:\n")
    for i in range(len(orden_alfa)):
        print(orden_alfa[i][0], ": ", orden_alfa[i][1])


t = '''Las unidades de estado solido SSD (Solid State Drive) javi
javi son una alternativa de los discos duros SSD. La gran diferencia es
que mientras los discos duros utilizan componentes mecanicos que se mueven,
las SSD almacenan los archivos en microchips con memorias flash interconectadas
entre si.
Casi podriamos considerarlos como una evolucion de las memorias USB.
Los SSD suelen utilizar memorias flash basadas en NAND, que como tambien
son no-volatiles mantienen la informacion almacenada cuando el disco se
desconecta. No tienen cabezales fisicos para grabar los datos, en su lugar
incluyen un procesador integrado para realizar operaciones relacionadas con
la lectura y escritura de datos. Estos procesadores,
llamados controladores, son los que toman las decisiones sobre como almacenar,
recuperar, almacenar en cache javi y limpiar los datos del disco, y su
eficiencia es uno de los factores que determinan la velocidad total de la
unidad. Ademas, al no depender del giro de un componente fisico, tambien se
logra una unidad mas silenciosa que los discos mecanicos. Evidentemente, estos
javi datos concretos de escritura y lectura de datos dependen siempre de los
diferentes modelos que hay en el mercado. Pero por general los discos duros
SSD siempre suelen javi ser mucho mas rapido que los mecanicos. De ahi
precisamente su alto precio. La gran preocupacion entorno los SSD siempre ha
estado en torno su durabilidad, sobre todo por la poca que tuvieron las
primeras unidades en llegar al mercado. La vida util de los discos de
estado solido depende directamente de la cantidad de datos que vas escribiendo
en el, ya que cada celda de un banco de sus memorias flash solo puede ser
escrita un numero de veces. De ahi precisamente su alto precio. La gran
preocupacion entorno los SSD siempre ha estado en torno su durabilidad,
sobre todo por la poca que tuvieron las primeras unidades en llegar al
mercado. La vida util de los discos de estado solido depende directamente de
la cantidad de datos que vas escribiendo en el, ya que cada celda de un banco
de sus memorias flash solo puede ser escrita un numero de veces.'''

if __name__ == "__main__":
    ejercicio(t)
