# Programa para multiplicar 2 numeros

# Solicitud de numeros al usuario
try:
    num1 = int(input("Ingrese el primer numero: "))
    num2= int(input("Ingrese el segundo numero: "))
    resultado = num1 * num2
    print(f"La multiplicacion de {num1} y {num2} es {resultado}")

except ValueError:
    
    print(f"Por favor, ingresa valores numericos y no otra cosa.")