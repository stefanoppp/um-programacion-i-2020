usr = input("Ingrese su nombre: ").lower()
gen = input("Ingrese su genero (mujer u hombre): ").lower()

if (gen == "mujer" and usr < "m") or (gen == "hombre" and usr > "n"):
    print("Es parte del grupo A")
else:
    print("Es parte del grupo B")
