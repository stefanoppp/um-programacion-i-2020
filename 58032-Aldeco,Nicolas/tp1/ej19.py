import json


class JsonMaker:
    def __init__(self, json, texto):
        self.direc_j = json
        self.direc_t = texto
        self.check_file_text
        self.load_json()

    def load_json(self):
        jfile = open(self.direc_j, 'w')
        texto = open(self.direc_t, 'r')
        dic_ventas = {}
        data = ['nombre',
                'nro_tarjeta',
                'cod_verficacion',
                'tipo_de_tarjeta',
                'monto',
                'descripcion']
        for line in texto:
            sales = line.split(',')
            num = 0
            for elem in sales:
                elem = self.clear(elem)
                temp = {data[num]: elem}
                num += 1
                dic_ventas.update(temp)
            json.dump(dic_ventas, jfile)
            jfile.write('\n')
            dic_ventas.clear()
        texto.close()
        jfile.close()

    @property
    def check_file_text(self):
        texto = []
        for i in (open(self.direc_t, 'r')):
            texto.append(i)
        for line in texto:
            sale = line.split(',')
            for word in sale:
                word = word.lstrip(' ')
                if word != '':
                    continue
                else:
                    raise Exception('Error de datos en >>' + self.direc_t)

    def clear(self, word):
        word = word.replace(' ', '')
        word = word.replace('\n', '')
        word = word.replace('{', '')
        word = word.replace('}', '')
        return word


class JsonMang(JsonMaker):
    def get_info_from_json(self, num_t):
        temp = []
        jfile = open(self.direc_j, 'r')
        for i in jfile:
            ventas = json.loads(i)
            if ventas['nro_tarjeta'] == num_t:
                temp.append(ventas['monto'])
                temp.append(ventas['descripcion'])
                temp.append(ventas['nombre'])
                temp.append(ventas['nro_tarjeta'])
                temp.append(ventas['cod_verficacion'])
        jfile.close()
        return temp


class TrajetaCredito:
    def __init__(self, name, number, cod_ver):
        self.name = name
        self.number = number
        self.cod_ver = cod_ver

    def __str__(self):
        return self.name+'\n'+self.number+'\n'+self.cod_ver


class Venta:
    def __init__(self, info):
        self.monto_de_venta = info[0]
        self.descp_venta = info[1]
        self.tarjeta = TrajetaCredito(info[2], info[3], info[4])

    def __str__(self):
        return self.monto_de_venta+'\n'+self.descp_venta+'\n'+str(self.tarjeta)


def main():
    files = JsonMang('./ventas2.json', './ventas2.txt')
    venta = Venta(files.get_info_from_json('456321789'))
    print(venta)


if __name__ == "__main__":
    main()
