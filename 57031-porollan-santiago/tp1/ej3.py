

if __name__ == "__main__":
    r = int(input("rango: "))
    print("impares hasta el " + str(r) + ": " + ", ".join([str(x) for x in range(r+1) if x%2 == 1]))
        