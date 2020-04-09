from ej_14 import Texto


class Interfaz():
    def interfaz(self, text):
        self.text = text
        x = Texto(self.text)
        print("Las 20 palabras que mas se repiten son:\n")
        for i in x.most_repeat():
            print(i)
        print("\n")
        print("Todas las palabras ordenadas de manera alfabetica y con la "
              "cantidad que se repiten son:\n")
        for i in x.contador_words().items():
            print(str(i[0]) + ": " + str(i[1]))


if __name__ == "__main__":
    text = """Consideremos ahora cómo se puede realizar esto. De 
              momento, vamos a hablar en términos generales, y
              usaremos el término porción para referirnos o bien
              a una página o un segmento, dependiendo si estamos
              empleando paginación o segmentación. Supongamos
              que se tiene que traer un nuevo proceso de memoria.
              El sistema operativo comienza trayendo únicamente
              una o dos porciones, que incluye la porción inicial
              del programa y la porción inicial de datos sobre
              la cual acceden las primeras instrucciones acceden.
              Esta parte del proceso que se encuentra realmente en
              la memoria principal para, cualquier instante de
              tiempo, se denomina conjunto residente del proceso.
              Cuando el proceso está ejecutándose, las cosas
              ocurren de forma suave mientras que todas las
              referencias a la memoria se encuentren dentro del
              conjunto residente. Usando una tabla de segmentos
              o páginas, el procesador siempre es capaz de
              determinar si esto es así o no. Si el procesador
              encuentra una dirección lógica.Aun asi todo no esta
              tan mal, solo hay que saber donde ubicar las cosas"""
    inter = Interfaz()
    inter.interfaz(text)
