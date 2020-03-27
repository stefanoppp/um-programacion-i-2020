"""
Ejercicio 14
Crear una variable con triple  comidas  que contenga  un texto  copiado de algún lugar de al
menos 20 líneas y hacer un conteo de palabras, al finalizar el conteo mostrar las 20 palabras
que más se repiten. Mostrar todas las palabras en orden alfabético y la cantidad que se repite.
"""

text = """

Internamente se distinguen algunas diferencias con los peces cartilaginosos:
mientras que éstos poseen una válvula espiral en el intestino, los osteíctios
presentan ciegos pilóricos y carecen de glándula rectal. En el sistema
respiratorio aparecen branquias dentro de una cámara branquial, y recubiertas
por un opérculo que muestra al exterior una sola abertura branquial a cada
lado. Ocasionalmente puede marcarse un preopérculo. Además, las branquias no
están separadas por septos. En algunos grupos, la vejiga natatoria se ha
transformado en un pulmón original, que le sirve además para flotar a
determinado nivel, o desplazarse verticalmente. Ambas estructuras, pulmón y
vejiga natatoria, son mutuamente excluyentes, es decir, cuando existe uno no
existe el otro, y viceversa. Presentan mayoritariamente boca terminal, capaz
de realizar movimientos muy precisos gracias a que poseen huesos dérmicos
articulados. Los dientes salen de algunos de estos huesos dérmicos y carecen
de reemplazo cuando se caen o rompen. Además, su aleta caudal es homocerca.
 Aparte de su esqueleto interno calcificado u osificado (la excepción es el
esturión, que lo tiene cartilaginoso como los condrictios), también poseen
huesos en la dermis de su tegumento en forma de escamas, lo que se conoce como
dermatoesqueleto. Estas escamas tienen un importante valor taxonómico, ya que
el tipo y número (especialmente en la línea lateral y transversalmente) son
usados como rasgos identificativos de los distintos grupos.
En relación a las aletas de los osteíctios, encontramos mayoritariamente un
par de aletas pelvianas y un par de aletas torácicas o pectorales (ambas
aletas son pares y simétricas en el cuerpo) y una o varias dorsales o una o
varias anales en el plano sagital, pero no de forma simétrica. También
presentan aleta caudal. Dependiendo de la posición de las aletas pelvianas y
torácicas, podemos distinguir cuatro tipos de osteíctios: abdominales (si las
aletas pelvianas se encuentran situadas por detrás de las torácicas),
torácicos (si están a la misma altura o ligeramente retrasadas), yugulares (si
están por delante) o ápodos (carecen de aletas pelvianas).

"""

text = text.replace("\n", " ")
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("(", "")
text = text.replace(")", "")
text = text.lower()
text = text.split(" ")
[text.remove("") for i in range(text.count(""))]

text.sort()


dicc = {}
for item in text:
    dicc[item] = text.count(item)


print("cantidad de palabras: " + str(len(text)))

print("\n\n\n20 palabras mas repetidas: ")
for item in sorted(dicc, key=dicc.get, reverse=True)[:20]:
    print(item + " " + str(dicc[item]))

print("\n\n\nTodas las palabras y sus cantidades: ")
for item in dicc.items():
    print(str(item[0]) + " " + str(item[1]))
