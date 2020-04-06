def p(r,l, c):
    if c != -1:
        print(l[c:])
        p(r, l, c-1)

def get_l(r):
    a = 1
    l = []
    for _ in range(1, r+1):
        l.insert(0, a)
        a+=2
    return l

if __name__ == "__main__":
    while 1:
        try:
            r = int(input("rango: "))
        except:
            print("ingrese numero")
        else:
            break
    p(r, get_l(r), r-1)
