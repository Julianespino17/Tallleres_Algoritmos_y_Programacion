Lote_de_naranjas=int(input("Lote de naranjas: "))
Docena=float(input("Docena: "))
total_ventas=float(input("Cantidad de las ventas: "))


total_ganancias=(Lote_de_naranjas/12)*Docena
porcentaje_ganancias=round((total_ventas-total_ganancias)*100)/total_ganancias


print("El porcentaje de ganancia fue de ",porcentaje_ganancias, "%")