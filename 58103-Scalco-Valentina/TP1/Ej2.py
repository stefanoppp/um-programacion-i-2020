pizza = int(input("Ingrese 1 si quiere pizza vegetariana y 2 si quiere pizza no vegetariana \n"))
if pizza == 1:
    print("Elija un ingrediente extra")
    ing = int(input("Ingrese 1 para PIMIENTO \nIngrese 2 para TOFU\n"))
    if ing == 1:
        print("Su pedido es:\nPizza vegetariana con muzzarela, tomate y pimiento")
    else:
        print("Su pedido es:\nPizza vegetariana con muzzarela, tomate y tofu")    
else:
    print("Elija un ingrediente extra")
    ing = int(input("Ingrese 1 para PEPERONI\nIngrese 2 para JAMON\nIngrese 3 para SALMON\n"))
    if ing == 1:
        print("Su pedido es:\nPizza no vegetariana con muzzarela, tomate y peperoni")
    elif ing == 2:
        print("Su pedido es:\nPizza no vegetariana con muzzarela, tomate y jamon")
    else:
        print("Su pedido es:\nPizza no vegetariana con muzzarela, tomate y salmon") 