
Altura = int(input("Ingrese su altura en centimetros: "))
Creditos = int(input("Cuantos creditos tienes?: "))

if Altura >=137 and Creditos >=10:
    print("Disfruta el juego") 
elif Creditos >=10 and Altura <137:
    print("No eres los suficientemente alto")
elif Altura >=137 and Creditos<10:
    print("No tienes suficientes creditos")
else:
    print("No eres los suficientemente alto ni tienes suficientes creditos")

