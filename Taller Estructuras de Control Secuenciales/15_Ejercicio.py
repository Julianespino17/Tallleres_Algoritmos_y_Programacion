#entrada
PVP=int(input("Ingrese el precio del producto sin descuento:"))
PVF=int(input("Ingrese el precio pagado por el producto con el descuento:"))
#caja negra
Desc=100-((PVF*100)/PVP)
#salida
print("El porcentaje del descuento hecho al producto es de:", Desc)
