def check(name, sex):
    aplha = list(map(chr, range(97, 123)))
    index = aplha.index(name[0].lower())
    if not name.isalpha():
        return('bad_name_input')
    if sex.lower() == 'f':
        if index < 13:
            return('GRUPO A')
        else:
            return('GRUPO B')
    elif sex.lower() == 'm':
        if index >= 13:
            return('GRUPO A')
        else:
            return('GRUPO B')
    else:
        return('bad_sex_input')


def main():
    name = input('Nombre>>')
    sex = input('Sexo(m o f)>>')
    print(check(name, sex))


if __name__ == '__main__':
    main()
