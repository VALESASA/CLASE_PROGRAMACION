a=int(input('ingrese un numero para saber si es primo '))
if a > 1:
    for i in range(2, int(a/2)+1):
         if (a % i) == 0:
            print("no es primo")
            break
    else:
        print("si es primo")

else:
    print("no es primo")
