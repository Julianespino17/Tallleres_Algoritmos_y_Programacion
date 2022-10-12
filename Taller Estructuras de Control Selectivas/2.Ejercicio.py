#entrada
Sueldo=float(input("Ingrese su sueldo:"))
#caja negra
Aumento_1=Sueldo*0.15
Aumento_2=Sueldo*0.12

if Sueldo<900000:
    nuevo_sueldo=Aumento_1+Sueldo
else:
    nuevo_sueldo=Aumento_2+Sueldo
#salida
print("Su nuevo sueldo sera:",nuevo_sueldo)