#entrada
salario_bruto=float(input("Ingrese su salario bruto mensual:"))
Departamento_1=float(input("Ingrese las ventas del departamento 1:"))
Departamento_2=float(input("Ingrese las ventas del departamento 2:"))
Departamento_3=float(input("Ingrese las ventas del departamento 3:"))
#caja negra
sdt=Departamento_1+Departamento_2+Departamento_3
ex=(sdt>0.33)

if Departamento_1>ex:
    ptd1=salario_bruto*0.20
else:
    ptd1=salario_bruto
if Departamento_2>ex:
    ptd2=salario_bruto*0.20
else:
    ptd2=salario_bruto
if Departamento_3>ex:
    ptd3=salario_bruto*0.20
else:
    ptd3=salario_bruto
#salida
print("Los vendedores del deparramento 1 recibiran ",ptd1)
print("Los vendedores del deparramento 2 recibiran ",ptd2)
print("Los vendedores del deparramento 3 recibiran ",ptd3)