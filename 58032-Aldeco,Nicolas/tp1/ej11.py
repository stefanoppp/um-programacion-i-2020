import os


class Course():
    def __init__(self):
        self.materias = {}
        self.total_credits = 0

    def input_info(self, num):
        for n in range(num):
            materia = input('Materia = ')
            credito = input('Creditos = ')
            if credito.isdigit():
                self.total_credits += int(credito)
            if materia.isalpha():
                dicc = {materia: credito}
                self.materias.update(dicc)
            else:
                print('bad_input')
                exit()
            os.system('clear')

    def print_all(self):
        maters = self.materias.keys()
        for mat in maters:
            print('En '+mat+' tiene '+self.materias[mat]+' creditos')
        print('Total de creditos = '+str(self.total_credits))


if __name__ == '__main__':
    obj = Course()
    num = int(input('Cuantas materias va ingresar?\n>>'))
    os.system('clear')
    obj.input_info(num)
    obj.print_all()
