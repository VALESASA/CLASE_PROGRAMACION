def factorial(num): 
    if num < 0: 
        print("Factorial negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num = int(input("Ingrese un numero para calcular su factorial: ")); 
print("El factorial de ", num ," es: ", factorial(num))
