#entrada
precio_computador=float(input("Ingrese el precio del computador: "))
valor_cuotas=float(input("Ingrese el valor de las cuotas: "))
#caja negro
total_cuotas=valor_cuotas*12
resta=total_cuotas-precio_computador
porcentaje_recargo=(resta*100)/precio_computador
#salida
print("Su porcentaje de recargo es del ", porcentaje_recargo, "%")
