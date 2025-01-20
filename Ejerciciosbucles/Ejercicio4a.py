# Se ingresan 3 valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 == numero2 == numero3:
    suma = numero1 + numero2
    resultado = suma * numero3
    print(f"El resultado es: {resultado}")
else:
    print("Los numeros no son todos iguales")
    
