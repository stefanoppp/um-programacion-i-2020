import json


class Reader():
    def __init__(self):
        self.json = open('./ventas.json', 'w')
        self.texto = open('./ventas.txt', 'r')

    def load_json(self):
        with open('ventas.json', 'w') as file:
            dic_ventas = {}
            data = ['nombre', 'monto', 'descripcion', 'formapago']
            for line in self.texto:
                sales = line.split(',')
                num = 0
                for elem in sales:
                    elem = self.clear(elem)
                    temp = {data[num]: elem}
                    num += 1
                    dic_ventas.update(temp)
                json.dump(dic_ventas, file)
                file.write('\n')
                dic_ventas.clear()

    @property
    def check_file(self):
        texto = []
        for i in (open('./ventas.txt', 'r')):
            texto.append(i)
        for line in texto:
            sale = line.split(',')
            for word in sale:
                word = word.lstrip(' ')
                if word != '':
                    continue
                else:
                    raise Exception('Error de datos en >> ./ventas.txt')

    def clear(self, word):
        word = word.lstrip(' ')
        word = word.rstrip('\n')
        return word


if __name__ == "__main__":
    obj = Reader()
    obj.check_file
    obj.load_json()
