class Piramide():
    def linea(self, num):
        for i in range(1, num+1, 2):
            for j in range(i, 0, -2):
                print(j, end=" ")
            print(" ")
        
if __name__ == "__main__":
    draw = Piramide()
    draw.linea(int(input("Ingrese un numero\n")))


