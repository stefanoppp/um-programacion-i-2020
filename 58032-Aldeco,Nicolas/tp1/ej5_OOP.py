class OddPyramid():
    def __init__(self, num):
        self.num = num

    @property
    def pyramid_of_odd(self):
        list_of_odd = []
        for odd in range(1, int(self.num)+1):
            if (odd % 2 != 0):
                list_of_odd.append(odd)
                list_of_odd.sort()
                list_of_odd.reverse()
                string_num = str(list_of_odd)
                string_num = string_num.replace(',', '')
                string_num = string_num.replace('[', '')
                string_num = string_num.replace(']', '')
                print(string_num)


if __name__ == '__main__':
    num = input('number = ')
    obj = OddPyramid(num)
    obj.pyramid_of_odd
