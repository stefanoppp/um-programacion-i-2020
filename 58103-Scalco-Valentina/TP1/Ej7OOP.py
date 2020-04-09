class Frase:
    def conteo(self, frase, letter):
        i = 0
        for letra in frase:
            if letra == letter:
                i += 1
        return("Hay", i ,"letras", letter, "en la frase ingresada")
                

def main():
    frase = input("Ingrese una frase\n").lower()
    letter = input("Ingrese una letra\n").lower()
    info = Frase()
    print(info.conteo(frase, letter))

if __name__ == "__main__":
    main()
