# Escribir un programa que pida ingresar la coordenada de un punto en el
#plano, es decir dos valores enteros x e y (distintos a cero).

#Posteriormente imprimir en pantalla en que cuadrante se ubica dicho
#punto. (1o Cuadrante si x > 0 Y y > 0 , 2o Cuadrante: x < 0 Y y > 0, etc.)

x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

if x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante")
elif x < 0 and y > 0:
    print ("El punto se encuentra en el segundo cuadrante")
elif x  < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante")
else:
    print("El punto se encuentra en el cuarto cuadrante")
    
