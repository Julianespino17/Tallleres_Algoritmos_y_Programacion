#entrada
lectura_an=float(input("Digite la lectura anterior: "))
lectura_ac=float(input("Digite la lectura actual: "))

#caja negra
r=(lectura_ac-lectura_an)
total=""

if r>=0 and r<=100:
    Total=r*4600
elif r>100 and r<=300:
    Total=r*80000
elif r>300 and r<=500:
    Total=r*100000
elif r>500:
    Total=r*120000
else:
    print("Error en los datos")
    quit()

#salida
print("El total a pagar es de "+str(Total))