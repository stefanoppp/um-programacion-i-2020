from random import randint
class Numeros():
    def __init__(self):
        self.dic = {}
        for key in range(1, 7):
            self.dic[key] = randint(1, 10)
    
    def show_items(self):
        while self.dic:
            max_key = 0
            for key in self.dic:
                if not max_key:
                    max_key = key
                    continue
                if self.dic[key] > self.dic[max_key]:
                    max_key = key
            print(self.dic.pop(max_key))


if __name__ == "__main__":
    numeros = Numeros()
    numeros.show_items()
