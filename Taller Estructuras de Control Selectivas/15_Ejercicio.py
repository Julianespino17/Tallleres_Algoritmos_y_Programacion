#entradas
me=int(input("Digite su edad en meses:"))
sx=str(input("Digite su sexo (M para mujer o H para hombre)):"))
hom=float(input("Digite  su porcentaje de hemoglobina:"))

#cajanegra
N=("Negativo para anemia")
P=("Positivo para anemia")

if me>=0 and me<=1:
    if hom>=13 and hom<=26:
        print(N)  #salidas
    elif hom<13:
        print(P)  #salidas
elif me>1 and me<=6:
    if hom>=10 and hom<=18:
        print(N)  #salidas
    elif hom<10:
        print(P)  #salidas
elif me>6 and me<=12:
    if hom>=11 and hom<=15:
        print(N)  #salidas
    elif hom<11:
        print(P)  #salidas
elif me>12 and me<=60:
    if hom>=11.5 and hom<=15:
        print(N)  
    elif hom<11.5:
        print(P)  #salidas
elif me>60 and me<=120:
    if hom>=12.6 and hom<=15.5:
        print(N)  #salidas
    elif hom<12.6:
        print(P)  #salidas
elif me>120 and me<=180:
    if hom>=13 and hom<=15.5:
        print(N)  #salidas
    elif hom<13:
        print(P)  #salidas
elif me>180:
    if sx=="M" or sx=="m":
        if hom>=12 and hom<=16:
            print(N)  #salidas
        elif hom<12:
            print(P)  #salidas
    elif sx=="H" or sx=="h":
        if hom>=14 and hom<=18:
            print(N)  #salidas
        elif hom<12:
            print("Es positivo para anemia")  #salida
else:
    print("Error en los datos")    #salida