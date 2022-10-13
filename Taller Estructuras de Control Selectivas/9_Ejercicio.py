#entradas
nombre=str(input("Ingrese su nombre:"))
monto=float(input("Ingrese el monto de su compra:"))

#caja negra
if monto<500000:
    p=monto
    descuento=0
elif monto>=500000 and monto<=100000:
    p=monto*0.05
    descuento=5
elif monto>100000 and monto<=700000:
    p=monto*0.11
    descuento=11
elif monto>700000 and monto<=1500000:
    p=monto*0.18
    descuento=18
elif monto>1500000:
    p=monto*0.25
    descuento=25

#salida
print(nombre,",Su monto de la compra es de ",monto," El monto a pagar es de ",p," por el descuento del ",descuento,"%")
