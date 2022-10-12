#entrada
P=int(input("Digite el dato P:"))
Q=int(input("Digite el dato Q:"))

#caja negra
expresion=(P**3 + Q**4 - 2*P**2)

if (expresion) > 680:
    print(P," y ",Q," Satisfacen la expresión")  #salida   
else: 
    print(P," y ",Q," no satisfacen la expresión")  #salida