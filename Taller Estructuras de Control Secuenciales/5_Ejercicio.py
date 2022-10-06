not_1=float(input("Digite la primera nota del parcial 1:"))
not_2=float(input("Digite la segunda nota del parcial 2:"))
not_3=float(input("Digite la tercera nota del parcial 3:"))
examen=float(input("Digite la nota de su examen final:"))
trabajo_final=float(input("Digite la nota de su trabajo final:"))

promedio_parciales=(not_1+not_2+not_3)/3
nota=(promedio_parciales*0.55)+(examen*0.33)+(trabajo_final*0.15)

print("Su calificacion final es: ",nota)