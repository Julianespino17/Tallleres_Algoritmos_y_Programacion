#entradas
d=int((input("Digite el dividendo:")))
di=int((input("Digite el divisor:")))
r=0
c=0
#caja negra 
while(d>=di):
    d=(d-di)
    r=d
    c=(c+1)
#salida
print("El coheficiente es:",c)
print("El residuo es:",r)