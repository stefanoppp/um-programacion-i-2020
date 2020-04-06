import random


class RandNum():

    def generate(self):
        self.dicc = {num: random.randint(1, 10) for num in range(20)}

    def sortDictioary(self):
        return sorted(self.dicc, key=self.dicc.get, reverse=True)

    def getDictionary(self):
        return self.dicc


"""
ejercicio12 = RandNum()

ejercicio12.generate()

for num in ejercicio12.sortDictioary():
    print("El",
          str(num+1) + "º numero que se genero es:",
          str(ejercicio12.getDictionary()[num])
          )
"""
