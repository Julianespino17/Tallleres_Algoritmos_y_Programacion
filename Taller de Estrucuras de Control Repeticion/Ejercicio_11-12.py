t=int(input("Digite el numero de personas encuestadas "))
i=int(0)
listasi=[]
listano=[]
listaaguardiente=[]
listaron=[]
listacerveza=[]
listatequila=[]
listawhisky=[]
listaotro=[]
listamasculino=[]
listafemenino=[]
listamenoresedadF=[]
listahombresag=[]
listaedadesc=[]
while i<t:
    i+=int(1)
    o=str(input("¿consume licor? "))
    b=str(input("su licor preferido "))
    m=int(input("su edad "))
    g=str(input("su sexo "))
    if o=="si":
        listasi.append(o)
    if o=="no":    
        listano.append(o)
    if b=="aguardiente":
        listaaguardiente.append(b)
    if b=="ron":
        listaron.append(b)
    if b=="cerveza":
        listacerveza.append(b)
        listaedadesc.append(m)
    if b=="tequila":
        listatequila.append(b)
    if b=="whisky":
        listawhisky.append(b)
    if b=="otro":
        listaotro.append(b)
    if b=="masculino":
        listamasculino.append(g)
    if b=="femenino":
        listafemenino.append(g)
    if g=="femenino" and g<18:
        listamenoresedadF.append(g)
    if g=="masculino" and b!="aguardiente" and 20<m<25:
        listahombresag.append(m)
    if i==t:
        break
Pwhisky=(len(listawhisky)*100)/t
r=sum(listaedadesc)
f=len(listacerveza)
procerv=float(r/f)
print("el total de personas que consumen licor es: ",len(listasi))    
print("el total de mujeres menores de edad es: ",len(listamenoresedadF))
print("el total de hombres que no consumen aguardiente y que tienen entre 20 y 25 es de: ", len(listahombresag))
print("el promedio de edades de las personas que consumen cerveza es de: ",procerv)
print("el porcentaje de personas que consumen wisky en relacion con el total encuestado es de: ",Pwhisky)