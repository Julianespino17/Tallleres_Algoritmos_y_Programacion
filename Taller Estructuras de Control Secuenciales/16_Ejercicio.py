import graphlib


Galones_Registrados=int(input("Ingrese la cantidad de galones registrados"))

S=Galones_Registrados*3.785
A=S*50000

print("se le tiene que cobrar al cliente:", A)