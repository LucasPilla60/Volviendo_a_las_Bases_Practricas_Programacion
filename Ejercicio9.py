#Escribe una funcion que calcule el factorial de un numero

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

