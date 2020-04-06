class Words():
    def __init__(self):
        self.texto = []
        for i in (open('./texto_ej14.txt', 'r')):
            self.texto.append(i)
        self.dic_of_words = {}

    def count_words(self):
        for sentence in self.texto:
            list_sentence = sentence.split(' ')
            for word in list_sentence:
                word = self.clean_word(word)
                if self.dic_of_words.get(word) is None:
                    tmp = {word: 1}
                    self.dic_of_words.update(tmp)
                else:
                    self.dic_of_words[word] += 1

    def clean_word(self, word):
        if word.isalnum():
            return word
        else:
            list_word = list(word)
            cleaned_word = ''
            for ch in list_word:
                if ch.isalnum():
                    cleaned_word += ch
            return cleaned_word

    @property
    def show_20_words(self):
        order = []
        for word in self.dic_of_words:
            temp = [self.dic_of_words[word], word]
            order.append(temp)
        order.sort()
        order.reverse()
        print('Las 20 palabras mas usadas:')
        for i in range(20):
            print(('>\'{word}\' aparece {times} vez/veces.').format(
                word=order[i][1],
                times=str(order[i][0])
            ))

    @property
    def show_all_words(self):
        order = []
        for word in self.dic_of_words:
            temp = [word, self.dic_of_words[word]]
            order.append(temp)
        order.sort()
        print('Palabras ordenadas alfabeticamente, junto con cant. de apar:')
        for words in order:
            print(('>\'{word}\' aparece {times} vez/veces.').format(
                word=words[0],
                times=str(words[1])
            ))


if __name__ == "__main__":
    obj = Words()
    obj.count_words()
    input('Mostrar 20 palablas mas mencionadas.')
    obj.show_20_words
    input('Mostrar palabras ordenadas alfabeticamente.')
    obj.show_all_words
