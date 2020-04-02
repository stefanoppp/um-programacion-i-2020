def odd_numbers(num):
    list_of_odd = []
    for odd in range(1, int(num)+1):
        if (odd % 2 != 0):
            list_of_odd.append(odd)
    string_num = str(list_of_odd)
    string_num = string_num.replace('[', '')
    string_num = string_num.replace(']', '')
    print(string_num)


def main():
    num = input('int = ')
    odd_numbers(num)


if __name__ == '__main__':
    main()
