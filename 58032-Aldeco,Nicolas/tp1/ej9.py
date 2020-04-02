def input_data():
    datos = ['Nombre', 'Edad', 'Direccion', 'Telefono']
    add_data = []

    for dato in datos:
        temp = input('{dat}:'.format(
            dat=dato
        ))
        add_data.append([dato, temp])
    return add_data


def main():
    dic = {}
    values = input_data()
    for par in values:
        dic[par[0]] = par[1]
    print('{name} tiene {age} anios, vive en \'{add}\' y su numero de telefono es \'{cel}\''.format(
        name=dic['Nombre'],
        age=dic['Edad'],
        add=dic['Direccion'],
        cel=dic['Telefono']
    ))


if __name__ == '__main__':
    main()
