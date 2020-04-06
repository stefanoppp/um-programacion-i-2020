import random as rand


class Numb():
    def ran(self):
        suma = 0
        temp = ''
        for i in range(9):
            num = rand.randint(1, 100)
            suma += num
            temp += str(num) + ' '
        temp2 = suma/10
        print('numeros generados:\n'+temp)
        print('Y el promedio es: '+str(temp2))


if __name__ == '__main__':
    obj = Numb()
    obj.ran()
