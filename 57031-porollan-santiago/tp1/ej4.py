def p(r):
    for x in range(1, r+1):
        print("*"*x)

if __name__ == "__main__":
    while 1:
        try:
            r = int(input("rango: "))
        except:
            print("ingrese numero")
        else:
            break
    p(r)
