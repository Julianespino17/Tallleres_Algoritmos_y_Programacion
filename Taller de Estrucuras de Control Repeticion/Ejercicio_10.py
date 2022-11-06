alturas=[]
while True:
    A=float(input("Digite las alturas de los estudiantes de la universidad:")) #entradas
    alturas.append(A)
    C=int(input("Desea continuar? Digite 1 para SI o 2 para NO "))  #entradas
    if(C==2):
        print("La altura mayor de la universidad es: ",max(alturas)) #salidas
        break