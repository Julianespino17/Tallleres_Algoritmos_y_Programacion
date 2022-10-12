#entrada
costo_kilovatio=int(input("Ingrese el costo por kilovatio: "))
Lectura_Anterior=int(input("Ingrese la lectura anterior en kilovatios:"))
Lectura_Actual=int(input("Ingrese la lectura actual en kilovatios:"))
#caja negra
T=(Lectura_Actual-Lectura_Anterior)/costo_kilovatio
#salida
print("Su monto total a pagar es de:",T)
