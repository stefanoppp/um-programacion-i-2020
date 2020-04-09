
class Lector():

    def __init__(self,path):

        self.frecuencia = {}
        self.documento = open(path,"r")
        self.texto = self.documento.read().lower()
        self.texto = self.texto.replace(","," ")
        self.lista = self.texto.split()

        for word in self.lista:
            count = self.frecuencia.get(word,0)
            self.frecuencia[word] = count + 1

    def mas_repetidas(self):        

        print("Las 20 palabras mas repetidas son: \n")
    
        for item in sorted(self.frecuencia, key=self.frecuencia.get, reverse=True)[:20]:
            print(item , " : " , str(self.frecuencia[item]))

    def conteo(self):
    
        frecuencia_list = list(self.frecuencia.keys())

        frecuencia_list.sort()

        print("\n")

        print("Todas las palabras y la cantidad que se repiten: \n")
 
        for words in frecuencia_list:
             print (words," : ", self.frecuencia[words])


"""Ejemplo
prueba = Lector("c:/Users/amaro/OneDrive/Documents/Programacion 1/TP1/documento.txt")

prueba.conteo()

prueba.mas_repetidas()

"""