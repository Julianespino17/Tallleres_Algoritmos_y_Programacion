enombre=[]
tpuntaje=[]
puni = puns = 0

while True:
    n=input("Ingrese su nombre ")  #entrada
    pf=float(input("Ingrese su puntaje final "))  #entrada
    enombre.append(n)  
    tpuntaje.append(pf)

    s=int(input("Desea ingresar mas datos? Digite 1 para SI y 2 para NO ")) #entrada
    if s==2:
        break

for x in range(len(tpuntaje)):
    if tpuntaje[x]<(sum(tpuntaje)/len(tpuntaje)): 
            puni=(puni+1)
        
    elif tpuntaje[x]>(sum(tpuntaje)/len(tpuntaje)):
            puns=(puns+1)

pori=round((puni*100)/len(tpuntaje),2)
pors=round((puns*100)/len(tpuntaje),2)


pm=0
punm=tpuntaje[0]

for x in range(len(tpuntaje)):
    if tpuntaje[x]>punm:
        punm=tpuntaje[x]
        pm=x
print("El estudiante con mayor puntaje es: ",enombre[pm])  #salidas
    
for x in range(len(tpuntaje)):    
    if tpuntaje[x]<punm:
        punm=tpuntaje[x]
        pm=x
print("El estudiante con menor puntaje es: ",enombre[pm])  #salidas

#salidas
print("El puntaje maximo obtenido es: ",max(tpuntaje))
print("El puntaje minimo obtenido es: ",min(tpuntaje))
print("El promedio de todos los puntajes es: ",round(sum(tpuntaje)/len(tpuntaje),2))
print(pori,'% fue inferior al promedio')
print(pors,'% fue superior al promedio')