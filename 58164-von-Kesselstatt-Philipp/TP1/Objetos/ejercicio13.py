import random


class RandomAverage():
    def generate(self):
        self.randList = [random.randint(1, 10) for n in range(10)]
        return self.randList

    def average(self):
        return sum(self.randList)/len(self.randList)


"""
ejercicio13 = RandomAverage()

for item in ejercicio13.generate():
    print(item)
print("promedio:", ejercicio13.average())
"""
