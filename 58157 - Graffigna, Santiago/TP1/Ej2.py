from os import system


print("\nBENVENUTI A PIZZERIA BELLA NAPOLI\n")

#ans=True
#while ans:
print("""
    1. Pizza Vegetariana: Pimiento o Tofu
    2. Pizza NO Vegetariana: Peperoni, Jamón o Salmón
    3. Salir
    """)
    
ans = input("Que desea elegir? ")

if ans=="1":

    ingrediente = input("Que ingrediente desea?\n 1. Pimiento\n 2. Tofu\n")

    if ingrediente == '1':
        ingrediente = "PIMIENTO"
    else:
        ingrediente = "TOFU"

    system('clear')
    print("Marcha una pizza Vegetariana con", ingrediente, "\nBuon Appetito!!\n")
    #ans = None

elif ans=="2":

    ingrediente = input("Que ingrediente desea?\n 1. Peperoni\n 2. Jamon\n 3. Salmon\n")

    if ingrediente == '1':
        ingrediente = "PEPERONI"
    elif ingrediente == '2':
        ingrediente = "JAMON"
    else:
        ingrediente = "SALMON"

    system('clear') 
    print("Marcha una pizza NO Vegetariana con", ingrediente, "\nBuon Appetito!!\n")
    #ans = None

elif ans=="3":
    print("\n Hasta pronto!!") 
    #ans = None
    
else:
    print("\n404")