

class Frase():
    def __init__(self, frase):
        self.valor = frase

    def obtener_conteo(self, letra):
        return self.valor.count(letra)

if __name__ == "__main__":
    frase = Frase(input("frase: "))
    letra = input("letra: ")
    print("la letra aparece ", frase.obtener_conteo(letra), " veces")