#Se ingresan por teclado 3 numeros, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda "Todos los numeros son menores a 10".

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 < 10 and numero2 < 10 and numero3 < 10:
    print(f"Todos los numeros son menores a 10")
else:
    print(f"No todos los numeros son menores a 10")
