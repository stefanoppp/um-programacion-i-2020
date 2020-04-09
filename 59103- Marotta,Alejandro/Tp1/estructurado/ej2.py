""" Ejercicio 2 
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
 Ingredientes vegetarianos: Pimiento y tofu. 
 Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no 
y todos los ingredientes que lleva.  """

def tipo(tipo):
    if tipo == 1:
        ing = int(input("Seleccione uno de los siguientes ingredientes: \n 1-Pimiento \n 2-Tofu \n"))
        t,i = vegetariana(ing)
        return t,i
        
    if tipo ==2:
        ing = int(input("Seleccione uno de los siguientes ingredientes: \n 1-Peperoni \n 2-Jamon \n 3-Salmon \n"))
        t,i = no_veg(ing)
        return t,i
        

def vegetariana(ing):       
    if ing == 1:
        return "Vegetariana","Pimiento"
    if ing == 2:
        return "Vegetariana","Tofu"

def  no_veg(ing):
    
    if ing == 1:
        return "Clasica","Peperoni"
    if ing == 2:
        return "Clasica","Jamon"
    if ing == 3:
        return "Clasica","Salmon"

def pizza(a,b):
    print ("Su pedido es una pizza "+a+" con Muzzarella, Tomate y "+b)


def start():
   selec = int(input("Seleecione el tipo de pizza \n 1-Vegetariana \n 2-Clasica \n"))
   
   a,b = tipo(selec)

   pizza(a,b)
   
   
start()