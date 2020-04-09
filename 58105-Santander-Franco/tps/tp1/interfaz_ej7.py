from ejercicio_7 import Phrase


class Interfaz():

    def interfaz(self):
        x = Phrase()
        phrase = str(input("Ingrese una frase:\n"))
        letter = str(input("Ingrese una letra:\n"))
        x.set_phrase(phrase)
        x.set_letter(letter)
        frase = x.get_phrase()
        letra = x.get_letter()
        print(x.repeat(frase.lower(), letra.lower()))


if __name__ == "__main__":
    inter = Interfaz()
    inter.interfaz()
