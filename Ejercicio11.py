#Escribe un programa que simule un cajero automatico:
#Debe permitir: 
# 1- Consultar saldo
# 2- Depositar dinero
# 3- Retirar dinero

saldo = 200000

opciones = {
    "1": lambda: print(f"El saldo actual es: {saldo}"),
    "2": lambda: depositar(),
    "3": lambda: retirar(),
    "4": lambda: exit()
}

def depositar():
    global saldo
    deposito = float(input("Ingrese la cantidad a depositar: "))
    saldo += deposito
    print(f"El saldo actual es: {saldo}")

def retirar():
    global saldo
    retiro = float(input("Ingrese la cantidad a retirar: "))
    if retiro > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= retiro
        print(f"El saldo actual es: {saldo}")

while True:
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    accion = opciones.get(opcion, lambda: print("Opcion no valida"))
    accion()


