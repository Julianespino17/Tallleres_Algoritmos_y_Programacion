#entrada
Caital_Invertido=float(input("Ingrese el capital invertido al banco:"))
porcentaje_Interes=float(input("Ingrese el porcentaje de intereses:"))
#caja negra
Interes_Total=porcentaje_Interes/100
dinero_total=Caital_Invertido*Interes_Total

if dinero_total>100000:
    total=Caital_Invertido+(2*dinero_total)
    print("Con el ",porcentaje_Interes,"%""de intereses, se tendra un total de:",total)  #salida
else:
    print("Sus intereses no sobrepasan los 100000 COP")  #salida