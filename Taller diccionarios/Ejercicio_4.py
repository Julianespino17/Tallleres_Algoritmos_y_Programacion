estudiantes = { 
"1": { 
"nombre": "Lorea", 
"nota": 8 
}, 
"2": { 
"nombre": "Markel", 
"nota": "4.2" 
}, 
"3": { 
"nombre": "Julen", 
"nota": 6.5 
} 
} 
e=10
lista_aprobados=[]
lista_suspendidos=[]
notas=[]
estudiantes={}
for c in range(0,10):
    nombre=input("ingrese nombre del estudiante:")
    enota=float(input("ingrese la nota del estudiante:"))
    estudiantes.update({c:{"nombre":nombre, "nota":enota}})
for i in estudiantes.keys():
    if (estudiantes[i]["nota"])<=5:
            lista_suspendidos.append(estudiantes[i]["nombre"])
    if (estudiantes[i]["nota"])>5:
        lista_aprobados.append(estudiantes[i]["nombre"])
    notas.append(estudiantes[i]["nota"])
media=(sum(notas))/e
print("Los estudiantes suspendidos fueron:",lista_suspendidos)
print("Los estudiantes aprobados fueron:",lista_aprobados)
print("El promedio de notas es de: ",media)