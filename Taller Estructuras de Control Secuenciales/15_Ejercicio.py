PVP=int(input("Ingrese el precio del producto sin descuento:"))
PVF=int(input("Ingrese el precio pagado por el producto con el descuento:"))

Desc=100-((PVF*100)/PVP)

print("El porcentaje del descuento hecho al producto es de:", Desc)