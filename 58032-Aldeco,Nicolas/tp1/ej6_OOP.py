class Prime():
    def __init__(self, num):
        self.num = int(num)

    def is_prime(self):
        for nums in range(2, self.num):
            if (self.num % nums == 0):
                return False
        return True

    @property
    def print_type(self):
        if self.is_prime():
            print('El numero es primo')
        else:
            print('El numero es no es primo')


if __name__ == '__main__':
    num = input('number = ')
    prime = Prime(num)
    prime.print_type
