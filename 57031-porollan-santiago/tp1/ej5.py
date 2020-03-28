def p(r,l, c=1):
    if c <= r:
        print(l[:c])
        p(r, l, c+1)

def get_l(r):
    a = 1
    l = []
    for _ in range(1, r+1):
        l.append(a)
        a+=2
    return l

if __name__ == "__main__":
    p(5, get_l(5))