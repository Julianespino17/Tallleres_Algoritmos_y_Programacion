#salida
hombres=int(input("Ingrese el numero de hombres:"))
mujeres=int(input("Ingrese el numero de mujeres:"))
#caja negra
total=hombres+mujeres
hombre_procentaje=(hombres/total)*100
mujeres_procentaje=(mujeres/total)*100
#salida
print("El porcentajes de hombres es ", hombre_procentaje, "%")
print("El porcentajes de mujeres es ", mujeres_procentaje, "%")
