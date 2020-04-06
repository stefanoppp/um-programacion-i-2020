
m = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio" ,
     7:"julio" ,8:"agosto" ,9:"septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}

if __name__ == "__main__":
    dia = input("dia: ")
    mes = input("mes: ")
    año = input("año: ")
    print(dia, " de ", m[int(mes)], " de ", año)