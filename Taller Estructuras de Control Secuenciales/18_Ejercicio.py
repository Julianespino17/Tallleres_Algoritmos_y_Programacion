#entrada
capital=float(input("Ingrese el capital "))
tasa_interes=float(input("Ingrese la tasa de interes "))
#caja negra
i=(tasa_interes*100)/(capital*4)
#salida
print("Su porcentaje anual de cobro por el prestamo de ",capital, " sera de ",i, "%")
