import math
#Entradas
lado_1=float(input("Ingrese lado 1: "))
lado_2=float(input("Ingrese lado 2: "))
lado_3=float(input("Ingrese lado 3: "))
#Caja negra
s= (lado_1+lado_2+lado_3)/2
area= math.sqrt(s*(s-lado_1)*(s-lado_2)*(s-lado_3))
#salida
print("El area es: "+str(area))
