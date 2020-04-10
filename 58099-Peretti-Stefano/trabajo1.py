                                                        # <<<EJERCICIO 1
class Curso():
    def __init__(self):
        nom = input ("Digite su nombre: ").upper()
        sex = input("Digite su sexo (M o F): ").upper()
        if nom.startswith (("A","B","C","D","E","F","G","H","I","J","K","L", "M")) and sex == "F" or nom.startswith(("N","O","P","Q","R","S","T","U","V","W","X","Y","Z")) and sex == "M":
            print("Su curso es el A")
        else:
            print("Su curso es el B")
course = Curso()
                                                        # EJERCICIO 2
class Pizza():
    def __init__(self):
        pizza = input("Buenos dias, desea una pizza vegetariana? Digite 'S' para confirmar o 'N' para rechazar: ").upper()
        if pizza == "S":
            print("Puede elegir uno de los siguientes condimentos para su pizza: pimiento o tofu")
            ingrediente_veg = input("Cual desea?: ").lower()
            if ingrediente_veg == "tofu" or ingrediente_veg=="pimiento":
                print("Ingrediente seleccionado")
                print("Su pizza vegetariana tiene tomate, mozzarella y ",ingrediente_veg)
            else:
                print("Ha digitado mal el ingrediente que desea")
        if pizza == "N":
            print("Puede elegir uno de los siguientes condimentos para su pizza: peperoni, jamon o salmon")
            ingrediente_noveg = input("Cual desea?: ").lower()
            if ingrediente_noveg=="peperoni" or ingrediente_noveg=="jamon" or ingrediente_noveg=="salmon":
                print("Ingrediente seleccionado")
                print("Su pizza no vegetariana tiene tomate, mozzarella y ",ingrediente_noveg)
            else:
                print("Ha digitado mal el ingrediente que desea")           
pizza_class = Pizza()

                                            # EJERICIO 3
class Numeros():
    def __init__(self):
        num = int(input("Digite un numero entero positivo: "))
        i =1
        while i<num:
            print (i,end=", ")
            i= i+2
        print(num)
calculadora = Numeros()

                                            # EJERCICIO 4
class Triangulo_asterisco():
    def __init__(self):
        altura = int(input("Indique la altura del triangulo: "))
        for i in range(altura):
            print("*"*(i+1))
trinag_asterisco= Triangulo_asterisco()
                                            # EJERCICIO 5 TERMINAR!!!!!!!!!!!!!
class Impresona_t_num():
    def __init__(self):
        numeropedido = int(input("Indique la altura del triangulo: "))
        i =1
        for i in range (numeropedido):
            for i in range (i):
                print(i, end=", ")
                i=i+2

        
triangulo_numerado= Impresona_t_num()
                                                
                                                # EJERCICIO 6
class Numero_Primo():
    def __init__(self):
        valor = True
        i=0
        num_primo = int(input ("Digite un numero: "))
        while i<num_primo and valor:
            if num_primo%2 ==0:
                valor = False
        if valor:
            print("Es primo")
        else:
            print("No es primo")
primo = Numero_Primo()

                                                # EJERCICIO 7
class Contadora_de_letras():
    text = input("Ingrese un texto: ").lower()
    letra = input("Ingrese letra que desee contar: ").lower()
    contador = 0
    i = 0
    for i in text:
        if i == letra:
            contador = contador+1
    print(contador)

                                            #    EJERCICIO 8
            
class Agenda():
    def __init__(self):
        materias = [ "Matemáticas: ", "Física: ", "Química: ", "Historia: ","Lengua: "]
        mat = int(input("Que nota sacaste en matematica: "))
        fisica = int(input("Que nota sacaste en fisica: "))
        quimica = int(input("Que nota sacaste en quimica: "))
        his = int(input("Que nota sacaste en historia: "))
        lengua = int(input("Que nota sacaste en lengua: "))
        mate = materias[0]
        fisi = materias[1]
        quimica2 = materias[2]
        historia = materias[3]
        lengua2 = materias[4]
        print(mate, mat )
        print(fisi, fisica)
        print(quimica2, quimica )
        print(historia, his )
        print(lengua2, lengua )
organizadora = Agenda()

                                        # EJERCICIO 9
class Diccionario():
    def __init__(self):
        diccionario = {}
        diccionario["nombre"] = input("dijite su nombre: ")
        diccionario["edad"] = input("dijite su edad: ")
        diccionario["direccion"] = input("dijite su direccion: ")
        diccionario["telefono"] = input("dijite su telefono: ")
        print(diccionario["nombre"]," tiene", diccionario["edad"], " años, vive en ", diccionario["direccion"], " y su numero de telefono es ", diccionario["telefono"])
llamado = Diccionario()

                                        # EJERCICIO 11
class Creditos():
    diccio={'Matematicas': 6, 'Fisica': 4, 'Quimica': 5 , "creditos totales":15} 
    print("Matematicas tiene ", diccio["Matematicas"], "creditos")
    print("Fisica tiene ", diccio["Fisica"], "creditos")
    print("Quimica tiene ", diccio["Quimica"], "creditos")
    print("El total de creditos del curso es de ", diccio["creditos totales"])

                                    # EJERCICIO 13
from random import *
class Num_random():
    def numero(min,max):
        if min>max:
            auxiliar = min
            min = max
            max = auxiliar
        return randint(min,max)
    i=0
    contador = 0
    while i<10:
        i = i+1
        print(numero(1,10))
        contador = contador+i
    print('El promedio es: ', contador/10)

                                    #  EJERCICIO 15
class Venta():
    diccionario = {}
    diccionario["nombre"] = input("dijite su nombre y apellido: ")
    diccionario["monto"] = input("dijite monto: ")
    diccionario["descripcion"] = input("dijite descripcion: ")
    diccionario["forma de pago"] = input("Contado o tarjeta: ")
    print(diccionario["nombre"],diccionario['monto'],diccionario['descripcion'], diccionario['forma de pago'])

                                    # EJERICCIO 16
class Venta():
    diccionario = {}
    diccionario["nombre"] = input("dijite su nombre y apellido: ")
    diccionario["monto"] = input("dijite monto: ")
    diccionario["descripcion"] = input("dijite descripcion: ")
    diccionario["forma de pago"] = input("Contado o tarjeta: ")
    print('Nombre y apellido: ',diccionario["nombre"],'Monto: ', diccionario['monto'], 'Descripcion: ',diccionario['descripcion'],'Forma de pago', diccionario['forma de pago'])    

