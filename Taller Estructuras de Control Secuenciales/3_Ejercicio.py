sueldo=float(input("Digite su sueldo base:"))

venta1=float(input("Digite la venta uno:"))
venta2=float(input("Digite la venta dos:"))
venta3=float(input("Digite la venta tres:"))

comision=(venta1+venta2+venta3)*0.10
total=(sueldo+comision)

print("El total de comision al mes:",comision)
print("Su sueldo total del mes fue de:",total)