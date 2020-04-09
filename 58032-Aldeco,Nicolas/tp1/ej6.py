def is_prime(num):
    for nums in range(2, num):
        if (num % nums == 0):
            return False
    return True


def main():
    number = int(input('number = '))
    res = is_prime(number)
    if res:
        tipo = 'Primo'
    else:
        tipo = 'No Primo'
    print('El numero ', str(number), ' es:', tipo)


if __name__ == '__main__':
    main()
