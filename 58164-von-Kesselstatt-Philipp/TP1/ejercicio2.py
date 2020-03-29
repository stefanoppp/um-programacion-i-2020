vegetariano = input("quere una pizza vegetariana? s/n")
print("eliga un ingrediente: ")

if vegetariano == "s":
    print("Pimiento")
    print("Tofu")
    pizza = "es vegetariana"

else:
    print("Peperoni")
    print("Jamón")
    print("Salmón")
    pizza = "no es vegetariana"

ingrediente = input("")

print("\nSu pizza " + pizza + " y lleva los siguentes ingredientes:")
print("Mozzarella")
print("Tomate")
print(ingrediente)
