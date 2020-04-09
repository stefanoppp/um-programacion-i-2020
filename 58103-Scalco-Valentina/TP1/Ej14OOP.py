
class Texto:

    def __init__(self):
        self.texto = '''
    Méliès intentó distribuir comercialmente Viaje a la Luna en Estados Unidos.
     Técnicos que trabajaban para Thomas Alva Edison lograron hacer copias de la 
     película y las distribuyeron por toda Norteamérica. A pesar de que fue un éxito,
     Méliès nunca recibió dinero por su explotación. El monopolio de la industria 
     cinematográfica (Edison en Estados Unidos y Pathé en Francia), junto con la llegada
     de la Primera Guerra Mundial, afectaron a su negocio, que fue declinando sin remedio.
     La producción masiva de Pathé y Gaumont complicó la competencia. El cineasta empezó a
     compartir cartel con Ferdinand Zecca, Louis Feuillade, el español Segundo de Chomón o David W.
     Griffith en Estados Unidos. Y por mucho que Pathé le ayudara en la producción de sus últimos 
     trabajos, la taquilla no hizo su parte.
    Para subsistir, Méliès se vio obligado a trabajar para Pathé y Edison. Firmó un contrato en el
     que se comprometía a proporcionar 300 metros de película semanales a este último, lo que le 
     forzaba a trabajar a marchas forzadas. Como se demostraría al poco tiempo, Méliès no estaba 
     hecho para la producción en cadena. Al contrario que los Pathé o los Edison, él no producía 
     películas como si fuesen churros. Para colmo de males, las obras que realizaba para Pathé sufrían
     amputaciones por parte de Ferdinand Zecca, el operador con más autoridad dentro de la productora y
     del que se rumoreaba sentía una gran envidia por Méliès. Empero, Zecca tiene el honor de ser el 
     primero en filmar una película dramática: Historia de un crimen, una fórmula que trataría de imitar 
     el genio parisino sin demasiado éxito tomando como argumento sucesos de actualidad como el caso Dreyfus.
    En 1913 se retiró de todo contacto con el cine, tras arruinarse, obligado a vender sus propiedades, 
     su estudio o sus muchos autómatas, e incluso que, en un ataque de desesperación, con una cerilla, 
     destruyera una colección de 500 negativos.
    De 1915 a 1923, Méliès montó numerosos espectáculos en uno de sus dos estudios cinematográficos 
    transformado en teatro. En 1923, acosado por las deudas, tuvo que vender propiedades y abandonar Montreuil.
     Muy a su pesar, Méliès dijo adiós al cine, pero siguió empeñado en continuar en el mundo del espectáculo,
     que era lo que le insuflaba vida. Montó una pequeña compañía de teatro junto con su yerno y su hija, pero
     fracasó una vez más. En 1925, cuando contaba sesenta y cuatro años, se casó en segundas nupcias con Jeanne
     D’Alcy, su musa, la actriz a la que hacía desaparecer en Escamoteo de una dama y a la que luego convertía
     en esqueleto. Casi no tenían donde caerse muertos, pero ella acababa de heredar un quiosco de juguetes 
     en la Estación de Montparnasse. Era un buen lugar donde sentar la cabeza después de una vida de lucha y sacrificio. '''
        self.palabras = {}
        self.word = {}

    def cuenta(self):
        for i in self.texto.lower().replace("," or "." or "\n").split(" "):
            if i not in self.palabras.keys():
                self.palabras[i] = 1
            else:
                self.palabras[i] += 1
        j= 0
        for i in sorted(self.palabras.items(), key=lambda x: x[1], reverse=True):
            if j == 20:
                break
            self.word[i[0]] = i[1]
            j += 1
        return self.word


def main():
    info = Texto()
    word = info.cuenta()
    for i in sorted(word.items()):
        print("'{}' se repitio {} veces".format(i[0], i[1]))


if __name__ == "__main__":
    main()