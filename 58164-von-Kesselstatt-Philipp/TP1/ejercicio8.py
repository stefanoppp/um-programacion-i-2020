notas = {"Matemáticas": 0, "Física": 0, "Química": 0, "Historia": 0, "Lengua": 0}

for item in notas:
    notas[item] = input("Cual es su nota en " + item + ": ")




for item in notas:
    print("En " + item + " has sacado " + notas[item])
