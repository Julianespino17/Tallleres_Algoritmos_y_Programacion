from datetime import datetime
hoy=datetime.now()
##de hoy 
dia_actual=hoy.day
mes_actual=hoy.month
año_actual=hoy.year
#entrada 
Fecha_nacimiento=input("Poner en formato dd/mm/yy:")
(dia,mes,año)=Fecha_nacimiento.split("/")
dia_nacimiento=int(dia)
mes_nacimiento=int(mes)
año_nacimiento=int(año)
#caja negra 
#CALULO EDAD
Ed=0
if (mes_actual>mes_nacimiento):
    Ed=año_actual-año_nacimiento
elif(mes_actual<mes_nacimiento):
    Ed=(año_actual-año_nacimiento)-1
elif(mes_actual==mes_nacimiento):
    if(dia_actual<dia_nacimiento):
        Ed=(año_actual-año_nacimiento)-1
    elif(dia_actual>dia_nacimiento):
        Ed=(año_actual-año_nacimiento)
    elif(dia_actual==dia_nacimiento):
        Ed=(año_actual-año_nacimiento)
print("la edad es:",Ed)
##signo
s=""
if((mes_nacimiento==11 and dia_nacimiento>=22) or (mes_nacimiento==12 and dia_nacimiento<=21)):
    s="sagitario"
elif((mes_nacimiento==12 and dia_nacimiento>=22) or (mes_nacimiento==1 and dia_nacimiento<=20)):
    s="capricornio"
elif((mes_nacimiento==1 and dia_nacimiento>=21) or(mes_nacimiento==2 and dia_nacimiento<=19)):
    s="acuario"
elif((mes_nacimiento==2 and dia_nacimiento>=20)or (mes_nacimiento==3 and dia_nacimiento<=19)):
    S="pisis"
elif((mes_nacimiento==3 and dia_nacimiento>=21) or(mes_nacimiento==4 and dia_nacimiento<=20)):
    s="aries"
elif((mes_nacimiento==4 and dia_nacimiento>=21) or(mes_nacimiento==5 and dia_nacimiento<=21)):
    s="tauro"
elif((mes_nacimiento==5 and dia_nacimiento>=22) or(mes_nacimiento==6 and dia_nacimiento<=21)):
    s="geminis"
elif((mes_nacimiento==6 and dia_nacimiento>=22) or(mes_nacimiento==7 and dia_nacimiento<=22)):
    s="cancer"
elif((mes_nacimiento==7 and dia_nacimiento>=23) or(mes_nacimiento==8 and dia_nacimiento<=23)):
    s="leo"
elif((mes_nacimiento==8 and dia_nacimiento>=24) or(mes_nacimiento==9 and dia_nacimiento<=22)):
    s="virgo"
elif((mes_nacimiento==9 and dia_nacimiento>=23) or(mes_nacimiento==10 and dia_nacimiento<=22)):
    s="libra"
elif((mes_nacimiento==10 and dia_nacimiento>=23) or(mes_nacimiento==11 and dia_nacimiento<=21)):
    s="escorpio"
#salida
print("Su signo es:",s)