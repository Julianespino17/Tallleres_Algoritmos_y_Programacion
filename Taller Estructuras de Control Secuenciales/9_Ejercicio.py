#entrada
numero_hora_trabajada=float(input("Ingrese numero de horas trabajadas:"))
precio_hora_trabajada=float(input("Ingrese el precio de la hora: "))
#caja negra
salario_neto=(numero_hora_trabajada*precio_hora_trabajada)*0.80
#salida
print("El salario neto es", salario_neto)
