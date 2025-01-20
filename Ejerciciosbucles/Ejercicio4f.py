#Escribir un programa en el cual dada una lista de tres valores numéricos distintos se calcule y muestre el menor y el mayor de ellos.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 == num2 == num3:
    print("Los numeros son iguales")

else:

    if num1 > num2 and num1 > num3:
        print(f"El numero mayor es {num1}")

    elif num2 > num1 and num2 > num3:
        print(f"El numero mayor es {num2}")
    
    elif num3 > num1 and num3 > num2:
        print(f"El numero mayor es {num3}")

    if num1 < num2 and num1 < num3:
        print(f"El numero menor es {num1}")

    elif num2 < num1 and num2 < num3:
        print(f"El numero menor es {num2}")
    
    elif num3 < num1 and num3 < num2:
        print(f"El numero menor es {num3}")
    
    else:
        print("Los numeros son iguales")
    

    