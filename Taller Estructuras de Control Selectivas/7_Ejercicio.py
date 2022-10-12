#entrada
r=float(input("Ingrese los km recorridos:"))
#caja negra
if r<=300:
    print("El valor a pagar es de 50000 COP")  
elif r>300 and r<=1000:
    p=((r-300)*30000)+70000
    print("El valor a pagar es de ",p," COP")  #salida
elif r>1000:
    p=((r-1000)*9000)+150000
    print("El valor a pagar es de ",p," COP")  #salida