def piramid(high):
    for num in range(1, int(high)+1):
        print('*'*num)


def main():
    high = input('altura = ')
    piramid(high)


if __name__ == '__main__':
    main()
