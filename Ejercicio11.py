#Escribe un programa que simule un cajero automatico:
#Debe permitir: 
# 1- Consultar saldo
# 2- Depositar dinero
# 3- Retirar dinero

saldo = 200000

while True:
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        print(f"El saldo actual es: {saldo}")
    elif opcion == "2":
        deposito = float(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        print(f"El saldo actual es: {saldo}")
    elif opcion == "3":
        retiro = float(input("Ingrese la cantidad a retirar: "))
        saldo -= retiro
        print(f"El saldo actual es: {saldo}")
    elif opcion == "4":
        break
    else:
        print("Opcion no valida")


