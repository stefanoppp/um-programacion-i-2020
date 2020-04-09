def Primo_NoPrimo(n): 
  

    if (n < 1 or n == 2): 
        return False
    if (n <= 3): 
        return True
  
    if (n % 2 == 0 or n % 3 == 0): 
        return False
  
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
  
    return True
  
numeroide = int(input("Ingresa un numero para chequear si es primo:\n"))

if (Primo_NoPrimo(numeroide)): 
    print("Es primo") 
else : 
    print("No es primo") 
      