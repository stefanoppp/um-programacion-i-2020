texto = '''
Los códigos de condición (también llamados indicadores) son bits cuyo valor lo asigna nor-
malmente el hardware de procesador teniendo en cuenta el resultado de las operaciones. Por ejem-
plo, una operación aritmética puede producir un resultado positivo, negativo, cero o desbordamien-
to. Además de almacenarse el resultado en sí mismo en un registro o en la memoria, se fija también
un código de condición en concordancia con el resultado de la ejecución de la instrucción aritméti-
ca. Posteriormente, se puede comprobar el código de condición como parte de una operación de
salto condicional. Los bits de código de condición se agrupan en uno o más registros. Normalmen-
te, forman parte de un registro de control. Generalmente, las instrucciones de máquina permiten
que estos bits se lean mediante una referencia implícita, pero no pueden ser alterados por una refe-
rencia explícita debido a que están destinados a la realimentación del resultado de la ejecución de
una instrucción.
En máquinas que utilizan múltiples tipos de interrupciones, se puede proporcionar un conjunto de
registros de interrupciones, con un puntero a cada rutina de tratamiento de interrupción. Si se utiliza
una pila para implementar ciertas funciones (por ejemplo llamadas a procedimientos), se necesita un
puntero de pila de sistema (véase el Apéndice 1B). El hardware de gestión de memoria, estudiado en
el Capítulo 7, requiere registros dedicados. Asimismo, se pueden utilizar registros en el control de las
operaciones de E/S.
En el diseño de la organización del registro de control y estado influyen varios factores. Un as-
pecto fundamental es proporcionar apoyo al sistema operativo. Ciertos tipos de información de con-
trol son útiles específicamente para el sistema operativo. Si el diseñador del procesador tiene un co-
nocimiento funcional del sistema operativo que se va a utilizar, se puede diseñar la organización de
registros de manera que se proporcione soporte por parte del hardware de características particulares
de ese sistema operativo, en aspectos tales como la protección de memoria y la multiplexación entre
programas de usuario.
'''
palabras = []
conteo = []
for i in texto.replace("-\n", "").replace("\n", " ").split(" "):
    if i not in palabras:
        palabras.append(i)
        conteo.append(1)
    else:
        conteo[palabras.index(i)] += 1
print(palabras, conteo)
