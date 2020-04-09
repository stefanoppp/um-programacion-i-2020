class Piramide():
    def linea(self, num):
        for i in range(num):
            print("*"*(i+1))
        
if __name__ == "__main__":
    draw = Piramide()
    draw.linea(int(input("Ingrese un numero\n")))