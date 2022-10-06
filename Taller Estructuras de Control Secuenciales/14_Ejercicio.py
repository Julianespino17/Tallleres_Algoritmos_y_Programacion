costo_kilovatio=int(input("Ingrese el costo por kilovatio: "))
Lectura_Anterior=int(input("Ingrese la lectura anterior en kilovatios:"))
Lectura_Actual=int(input("Ingrese la lectura actual en kilovatios:"))

T=(Lectura_Actual-Lectura_Anterior)/costo_kilovatio

print("Su monto total a pagar es de:",T)