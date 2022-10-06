#entradas
#notas matematicas
examen_matematicas=float(input("Ingrese el examen de matematicas:")) 
tarea1_matematicas=float(input("Ingrese la tarea 1 de matematicas:"))
tarea2_matematicas=float(input("Ingrese la tarea 2 de matematicas:"))
tarea3_matematicas=float(input("Ingrese la tarea 3 de matematicas:"))
#notas fisica
examen_fisica=float(input("Ingrese el examen de fisica:")) 
tare1_fisica=float(input("Ingrese la tarea 1 de fisica:"))
tarea2_fisica=float(input("Ingrese la tarea 2 de fisica:"))
#notas quimica
examen_quimica=float(input("Ingrese el examen de quimica:")) 
tarea1_quimica=float(input("Ingrese la tarea 1 de quimica:"))
tarea2_quimica=float(input("Ingrese la tarea 2 de quimica:"))
tarea3_quimica=float(input("Ingrese la tarea 3 de quimica:"))
#caja negra
#promedios notas matematicas
prom_tareas_matematicas=(tarea1_matematicas+tarea2_matematicas+tarea3_matematicas)/3  
prom_matematicas=((examen_matematicas*0.90)+(prom_tareas_matematicas*0.10))
#promedios notas fisica
prom_tarea_fisica=(tare1_fisica+tarea2_fisica)/2     
prom_fisica=((examen_fisica*0.80)+(prom_tarea_fisica*0.20))
#promedios notas quimica
prom_tareas_quimica=(tarea1_quimica+tarea2_quimica+tarea3_quimica)/3  
prom_quimica=((examen_quimica*0.90)+(prom_tareas_quimica*0.10))
#promedio general
prom_general=((prom_matematicas+prom_fisica+prom_quimica)/3)
#salidas
print("Su promedio de matematicas es de: ",prom_matematicas)
print("Su promedio de fisica es de: ",prom_fisica)
print("Su promedio de quimica es de: ",prom_quimica)
print("Su promedio general de las tres materias es de: ",prom_general)