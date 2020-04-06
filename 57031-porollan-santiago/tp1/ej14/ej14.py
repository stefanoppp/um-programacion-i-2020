import re

def get_words():
    texto = """ """
    for line in open("texto"):
        texto += line + " "
    words = {}
    for word in re.split(" |, |\n", texto):
        if word not in words and len(word) > 3:
            words[word] = texto.count(word)
    return words

def fix_size(words):
    while len(words) > 20:
        min_key = ""
        for word in words:
            if not min_key:
                min_key = word
            elif words[word] < words[min_key]:
                min_key = word
        words.pop(min_key)
    return words

def show_words(words):
    while words:    
        first = ""
        for word in words:
            if not first:
                first = word
            elif word.lower() < first.lower():
                first = word
        print(first," se repite: ", words[first], " veces")
        words.pop(first)

if __name__ == "__main__":
    words = get_words()
    words = fix_size(words)
    show_words(words)
