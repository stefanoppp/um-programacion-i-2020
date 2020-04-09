class CharTimes():
    def __init__(self, frase, letra):
        self.frase = frase
        self.letra = letra

    @property
    def char_times(self):
        num = 0
        for let in self.frase:
            if let == self.letra:
                num += 1
        print('El caracter \'{let}\' aparece {times} veces'.format(
            let=self.letra, times=str(num)
        ))


if __name__ == '__main__':
    frase = input('Decime un frase:\n>')
    letra = input('Una letra:\n>')
    obj = CharTimes(frase, letra)
    obj.char_times
