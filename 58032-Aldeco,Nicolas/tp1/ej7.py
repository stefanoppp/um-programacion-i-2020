def char_times(frase, letra):
    num = 0
    for let in frase:
        if let == letra:
            num += 1
    print('El caracter \'{let}\' aparece {times} veces'.format(
        let=letra, times=str(num)
    ))


def main():
    frase = input('Decime un frase:\n>')
    letra = input('Una letra:\n>')
    char_times(frase, letra)


if __name__ == '__main__':
    main()
