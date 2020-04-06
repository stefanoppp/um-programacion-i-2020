

if __name__ == "__main__":
    creditos = {"matematicas": 6, "física": 5, "quimica": 4}
    total = 0
    for materia in creditos:
        print(materia, " ",creditos[materia])
        total += creditos[materia]
    print("total del curso: ", total)