from random import randint


if __name__ == "__main__":
    dic = {}
    for key in range(1, 7):
        dic[key] = randint(1, 10)
    while dic:
        max_key = 0
        for key in dic:
            if not max_key:
                max_key = key
                continue
            if dic[key] > dic[max_key]:
                max_key = key
        print(dic.pop(max_key))
