#entradas
C=int(input("Ingrese su categoria:"))
b=int(input("Ingrese su salario bruto:"))

#cajanegra
if C==1:
    Au=0.10
elif C==2:
    Au=0.15
elif C==3:
    Au=0.20
elif C==4:
    Au=0.40
elif C==5:
    Au=0.60

#salidas
print("De la categoria ",C,"Su nuevo sueldo sera ",b*Au)