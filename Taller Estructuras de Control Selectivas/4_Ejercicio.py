#entrada
Mc=float(input("Ingrese el monto de la compra:"))
#caja negra
if Mc>5000000:
    Id=Mc*0.55
    Pbd=Mc*0.30
    Rf=Mc-(Id+Pbd)
else:
    Id=Mc*0.70
    Rf=Mc-Id
    Pbd=0

ri=Rf*0.20   
#salida
print("La suma de:",Mc, "se pagara con:",Id," por parte de los fondos de la empresa")
print(Rf,"Se pagara a credito, con el 20""%" "de intereses para un total de:",ri)
print("El prestamo del banco sera de:",Pbd)