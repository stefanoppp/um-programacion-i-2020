""" Ejercicio 14
Crear una variable con triple comillas que contenga un texto copiado de algún lugar de al
menos 20 líneas y hacer un conteo de palabras, al finalizar el conteo mostrar las 20 palabras
que más se repiten. Mostrar todas las palabras en orden alfabético y la cantidad que se repite.
 """


frecuencia = {}
documento = open("c:/Users/amaro/OneDrive/Documents/Programacion 1/TP1/documento.txt","r")
texto = documento.read().lower()
texto = texto.replace(","," ")
lista = texto.split()


 
for word in lista:
    count = frecuencia.get(word,0)
    frecuencia[word] = count + 1

print("Las 20 palabras mas repetidas son: \n")
    
for item in sorted(frecuencia, key=frecuencia.get, reverse=True)[:20]:
    print(item , " : " , str(frecuencia[item]))

     
frecuencia_list = list(frecuencia.keys())

frecuencia_list.sort()

print("\n")

print("Todas las palabras y la cantidad que se repiten: \n")
 
for words in frecuencia_list:
    print (words," : ", frecuencia[words])

