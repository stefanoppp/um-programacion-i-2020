
name = input('Nombre>>')
sex = input('Sexo(m o f)>>')

aplha = list(map(chr, range(97, 123)))
index = aplha.index(name[0].lower())

if name.isalnum():
    print('bad_name_input')
    exit()
if sex.lower() == 'f':
    if index < 13:
        print('GRUPO A')
    else:
        print('GRUPO B')
elif sex.lower() == 'm':
    if index >= 13:
        print('GRUPO A')
    else:
        print('GRUPO B')
else:
    print('bad_sex_input')
