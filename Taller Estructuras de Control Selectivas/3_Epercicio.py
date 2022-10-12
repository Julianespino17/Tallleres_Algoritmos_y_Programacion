#entrada
A=int(input("Digite el dato a:"))
B=int(input("Digite el dato b:"))
C=int(input("Digite el dato c:"))
D=int(input("Digite el dato d:"))
#caja negra
if D==0:
    p=(A-C)**2
elif D>0:
    p=((A-B)**3)/D
#salida
print("El resultado es ",p)