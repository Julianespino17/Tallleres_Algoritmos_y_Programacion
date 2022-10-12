#entrada
A=int(input("Ingrese a:"))
B=int(input("Ingrese b:"))
C=int(input("Ingrese c:"))
D=int(input("Ingrese d:"))
#caja negra
if C>=5:
    Q=(B+1)
    C=0
    D=0
    print(str(A)+str(Q)+str(C)+str(D))  #salida
elif C<5:
    C=0
    D=0
    print(str(A)+str(B)+str(C)+str(D))  #salida