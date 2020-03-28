impares = lambda num: [x for x in range(num+1) if x%2 == 1]

if __name__ == "__main__":
    while 1:
        try:
            r = int(input("rango: "))
        except:
            print("ingrese numero")
        else:
            break
    print("impares hasta el ", r, ": ")
    im = impares(r)
    for num in im[:-1]:
        print(num, end=", ")
    print(im[-1])
        
        