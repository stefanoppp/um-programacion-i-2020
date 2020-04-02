class Materias():
    def __init__(self):
        self.materias = ['Matemáticas',
                         'Física',
                         'Química',
                         'Historia',
                         'Lengua']

    def materias_and_notas(self):
        final_mat = []
        for mat in self.materias:
            nota = input('{mater} = '.format(mater=mat))
            temp = [mat, nota]
            final_mat.append(temp)
        return final_mat


if __name__ == '__main__':
    obj = Materias()
    notas = obj.materias_and_notas()
    for par in notas:
        print('En {mat} se saco: {note}'.format(
            mat=par[0], note=par[1]
        ))
