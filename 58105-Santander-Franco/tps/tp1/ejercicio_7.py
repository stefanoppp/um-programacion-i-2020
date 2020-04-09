class Phrase():
    def __init__(self):
        self.phrase = ''
        self.letter = ''

    def get_phrase(self):
        return self.phrase

    def set_phrase(self, phrase):
        self.phrase = phrase

    def get_letter(self):
        return self.letter

    def set_letter(self, letter):
        self.letter = letter

    def repeat(self, phrase, letter):
        num = int(phrase.count(letter))
        if num == 0:
            return ("No se repite la letra ingresada")
        elif num == 1:
            return ("La letra " + str(letter) + " se repite " + str(num) +
                    " vez")
        else:
            return("La letra " + str(letter) + " se repite " + str(num) +
                   " veces")


if __name__ == "__main__":
    hola = Phrase()
