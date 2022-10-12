#entrada
TF=float(input("Ingrese la temperatura:"))
#caja negra 
deporte=""
if(TF>85  and  TF<=100): 
    deporte="Natacion" 
elif(TF>=71  and  TF<=85): 
    deporte="Tenis"
elif(TF>=33  and  TF<=20):
    deporte="Golf"
elif(TF>=11  and  TF<=32):
    deporte="Esqui"
elif(TF>-5  and  TF<=10):
    deporte="Marcha"
else:
    deporte="🤔No hay un deporte para esa temperatura"
#salida
print("El deporte a practicar es:",deporte)