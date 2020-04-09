class Texto():
    def __init__(self, text):
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.replace("\n", "")
        text = text.lower()
        text = text.split(" ")
        self.text = text
        self.text.sort()
        self.dicc = {}
        for i in self.text:
            self.dicc[i] = self.text.count(i)

    def contador_words(self):
        return self.dicc

    def most_repeat(self):
        return(sorted(self.dicc, key=self.dicc.get, reverse=True)[:20])


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
    hola = Texto(text)
