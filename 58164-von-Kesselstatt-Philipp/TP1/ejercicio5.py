def ejercicio5(cantidad):

    for n in range(1, int(cantidad)+1):
        x = ""
        for num in range(1, n*2+1, 2):
            x += str(num)
        print(x[::-1])


"""
ejercicio5(
           int(input("ingrese un numero  "))
          )
"""
