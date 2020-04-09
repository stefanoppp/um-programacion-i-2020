class Pyramid():
    def make_pyramid(self, high):
        for num in range(1, int(high)+1):
            print('*'*num)


if __name__ == '__main__':
    obj = Pyramid()
    obj.make_pyramid(input('altura = '))
