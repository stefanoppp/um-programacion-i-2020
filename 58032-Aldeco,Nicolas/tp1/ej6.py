def is_prime(num):
    for nums in range(2, num):
        if (num % nums == 0):
            return False
    return True


number = int(input('number = '))
res = is_prime(number)
if res:
    tipo = 'Primo'
else:
    tipo = 'No Primo'
print('El numero ', str(number), ' es:', tipo)
