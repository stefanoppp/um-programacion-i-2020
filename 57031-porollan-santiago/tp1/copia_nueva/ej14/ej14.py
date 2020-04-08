import re


class Words():
    def __init__(self):
        self.get_words()

    def get_words(self):
        texto = """ """
        for line in open("texto"):
            texto += line + " "
        words = {}
        for word in re.split(" |, |\n", texto):
            if word not in words and len(word) > 3:
                words[word] = texto.count(word)
        self.words = words

    def fix_size(self):
        while len(self.words) > 20:
            min_key = ""
            for word in self.words:
                if not min_key:
                    min_key = word
                elif self.words[word] < self.words[min_key]:
                    min_key = word
            self.words.pop(min_key)

    def show(self):
        while self.words:    
            first = ""
            for word in self.words:
                if not first:
                    first = word
                elif word.lower() < first.lower():
                    first = word
            print(first," se repite: ", self.words[first], " veces")
            self.words.pop(first)


if __name__ == "__main__":
    words = Words()
    words.fix_size()
    words.show()
