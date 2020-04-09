import random

dict_of_randoms = {}
for x in range(10):
    dict_of_randoms.setdefault(random.randint(0, 10))

ordered_randoms = sorted(dict_of_randoms, reverse = True)
print(ordered_randoms)
