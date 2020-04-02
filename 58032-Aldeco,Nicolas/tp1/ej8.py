def input_materias():
    materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    final_mat = []

    for mat in materias:
        nota = input('{mater}='.format(mater=mat))
        temp = [mat, nota]
        final_mat.append(temp)

    return final_mat


def main():
    notas = input_materias()
    for par in notas:
        print('En {mat} se saco: {note}'.format(
            mat=par[0], note=par[1]
        ))


if __name__ == '__main__':
    main()
