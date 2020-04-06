

def es_primo(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


if __name__ == "__main__":
    while 1:
        try:
            num = int(input("numero: "))
        except:
            print("ingrese numero")
        else:
            break
    
    if es_primo(num):
        print("el numero es primo")
    else:
        print("el numero no es primo")
