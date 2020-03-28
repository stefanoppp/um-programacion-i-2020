
menu = {1:"pimiento", 2:"tofu", 3:"peperoni", 4:"jamon", 5:"salmon"}
ingredientes = ["tomate", "mozzarella"]

def agregar_ingrediente(ingredientes, ingrediente):
    if ingrediente not in ingredientes:
        print("seleccionado ", ingrediente)
        ingredientes.append(ingrediente)
    else:
        print(ingrediente, " ya se encontraba seleccionado")

if __name__ == "__main__":
    # preguntar si es vegetariana
    es_vegetariana = input("pizza vegetariana? si, no: ")
    es_vegetariana = 3 if es_vegetariana == "si" else 6

    #ingresar ingredientes
    while 1:

        for x in range(1, es_vegetariana):
            print(x, ": ", menu[x])
        ingrediente = input("stop o seleccionar del menu: ")

        try:
            ingrediente = int(ingrediente)
        except:
            for x in range(1, es_vegetariana):
                if menu[x] == ingrediente:
                    agregar_ingrediente(ingredientes, ingrediente)
                    break
                if x == es_vegetariana - 1:
                    print("no se ha encontrado ", ingrediente, " en el menu")
        else:
            if ingrediente < es_vegetariana:
                    agregar_ingrediente(ingredientes, menu[ingrediente])
            else:
                print("no se ha encontrado ", ingrediente, " en el menu")
        if ingrediente == "stop":
            break

    # mostrar pizza
    es_vegetariana = "vegetariana" if es_vegetariana == 3 else "no vegetariana"
    print("Pizza ", es_vegetariana)
    print("Ingredientes: ")
    for i in ingredientes:
        print(i, " ")
