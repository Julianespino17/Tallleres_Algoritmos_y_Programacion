A=0
D=0
G=0
while True:
    t=int(input(""))
    if(t==1):
        A=(A+1)
    elif(t==2):
        G=(G+1)
    elif(t==3):
        D=(D+1)
    elif(t==4):
        break
print(f"MUITO OBRIGADO Alcool: {A}  Gasolina: {G}  Diesel: {D}")