#entrada
a=float(input("Digite el valor de a:"))
b=float(input("Digite el valor de b:"))
c=float(input("Digite el valor de c:"))

#caja negra
d=b**2-4*a*c

if d==0:
    x1=-b/(2*a)
    print("X1 = X2 = ",x1)  #salidas
elif d>0:
    x1=(-b+(b**2-4*a*c)**1/2)/(2*a)
    x2=(-b-(b**2-4*a*c)**1/2)/(2*a)
    print("X1=",x1)  #salida
    print("X2=",x2)  #salida
elif d<0:
    print("No tiene solucion en los reales")  #salida