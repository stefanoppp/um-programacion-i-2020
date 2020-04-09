import random as rand


class Rand():
    def __init__(self):
        self.numbers = {}

    def make_dicc(self, times):
        for i in range(times):
            r_numb = rand.randint(1, 10)
            temp = {i: r_numb}
            self.numbers.update(temp)

    def order_numbers(self):
        all_numbers = list(self.numbers.values())
        all_numbers.sort()
        all_numbers.reverse()
        temp = len(list(self.numbers.keys()))
        for i in range(temp):
            temp2 = all_numbers[i]
            self.numbers[i] = temp2

    @property
    def print_dicc(self):
        print(str(self.numbers)+'\n')


if __name__ == '__main__':
    obj = Rand()
    num = int(input('times = '))
    obj.make_dicc(num)
    print('Diccionario desordenado:\n')
    obj.print_dicc
    obj.order_numbers()
    print('Diccionario ordenado:\n')
    obj.print_dicc
