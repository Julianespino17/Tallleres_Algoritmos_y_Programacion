#sentrada
Monto_de_compra=float(input("Ingrese el monto de la compra:"))
#caja negra
if Monto_de_compra>5000000:
    Invertir_dinero=Monto_de_compra*0.55
    Prestamo=Monto_de_compra*0.30
    resto_fabricante=Monto_de_compra-(Invertir_dinero+Prestamo)
else:
    Invertir_dinero=Monto_de_compra*0.70
    resto_fabricante=Monto_de_compra-Invertir_dinero
    pbd=0

ri=resto_fabricante*0.20   
#salida
print("La suma de ",Monto_de_compra, "se pagara con ",Invertir_dinero," por parte de los fondos de la empresa")
print(resto_fabricante," se pagara a credito, con el 20% de intereses para un total de ",ri)
print("El prestamo del banco sera de ",pbd)