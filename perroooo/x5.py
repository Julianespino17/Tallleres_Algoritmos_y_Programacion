#entrada
salario_bruto=float(input("Ingrese su salario bruto mensual:"))
Departamento_1=float(input("Ingrese las ventas del departamento 1:"))
Departamento_2=float(input("Ingrese las ventas del departamento 2:"))
Departamento_3=float(input("Ingrese las ventas del departamento 3:"))
#caja negra
sdt=(Departamento_1+Departamento_2+Departamento_3)/3
ex=sdt*0.33

if Departamento_1>ex:
    d1=salario_bruto*0.20
else:
    d1=salario_bruto
if Departamento_2>ex:
    d2=salario_bruto*0.20
else:
    d2=salario_bruto
if Departamento_3>ex:
    d3=salario_bruto*0.20
else:
    d3=salario_bruto
#salida
print("Los vendedores del deparramento 1 recibiran ",d1)
print("Los vendedores del deparramento 2 recibiran ",d2)
print("Los vendedores del deparramento 3 recibiran ",d3)