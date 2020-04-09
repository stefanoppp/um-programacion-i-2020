def get_date(fecha):
    values = fecha.split('/')
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril',
             'Mayo', 'Junio', 'Julio', 'Agosto',
             'Septiembre', 'Octubre', 'Noviembre',
             'Diciembre']
    for mm in range(12):
        if ((int(values[1])-1) == mm):
            mes = meses[mm]
    return('{d} de {m} de {a}').format(
        d=values[0], m=mes, a=values[2])


def main():
    fecha = input('dd/mm/aaaa = ')
    print(get_date(fecha))


if __name__ == '__main__':
    main()
