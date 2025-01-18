#Suma todos los numeros pares del 1 al 50

suma = 0
for i in range(1,51):
    if i % 2 == 0:
        suma += i

print(f"La suma de los numeros pares del 1 al 50 es: {suma}")
