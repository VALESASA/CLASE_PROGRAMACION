
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

num = int(input("Ingrese primer numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese segundo numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese tercer numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese cuarto numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese quinto numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese sexto numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese septimo numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese octavo numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese noveno numero: ")); 
print("El factorial es: ", factorial(num))
num = int(input("Ingrese decimo numero: ")); 
print("El factorial es: ", factorial(num))
