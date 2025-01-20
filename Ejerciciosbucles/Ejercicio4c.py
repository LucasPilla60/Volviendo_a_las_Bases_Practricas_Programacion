# Se ingresan por teclado tres números, si al menos uno de los valores
#ingresados es menor a 10, imprimir en pantalla la leyenda
#"Alguno de los números es menor a diez".

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 < 10 or numero2 < 10 or numero3 < 10:
    print(f"Alguno de los numeros es menor a 10")
else:
    print(f"Ninguno de los numeros es menor a 10")
