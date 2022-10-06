nombre_del_trabajor=str(input("Ingrese el nombre del trabajador "))
horas_normales=float(input("Ingrese el numero de horas normales trabajadas "))
pago_hora=float(input("Ingrese el pago de una hora normal "))
horas_extras=float(input("Ingrese el numero de horas extras trabajadas "))
sueldo_base=float(input("Ingrese el sueldo base "))
numero_hijos=int(input("Ingrese el numero de hijos "))


pago_horas_extras=(pago_hora*0.25)*horas_extras

paro_forzado=sueldo_base*0.05
politicas_habituales=sueldo_base*0.02
caja_ahorro=sueldo_base*0.07

de=paro_forzado+politicas_habituales+caja_ahorro

actualizacion_academica=250000
pago_hora=180000
hijos=numero_hijos*173000

asig=actualizacion_academica+pago_hora+hijos

sn=(sueldo_base+pago_horas_extras+asig)-de


print("Señor",nombre_del_trabajor,"Sus asignaciones seran de ", asig)
print("Señor",nombre_del_trabajor,"Sus deduciones seran de", de)
print("Señor",nombre_del_trabajor,"Su salario neto sera de ", sn)