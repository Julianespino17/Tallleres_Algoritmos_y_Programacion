#entrada
pesoc=int(input("Digite la cantidad de COP:"))

#caja negra
b100=(pesoc-pesoc%100000)/100000
pesoc=pesoc%100000
b50=(pesoc-pesoc%50000)/50000
pesoc=pesoc%50000
b20=(pesoc-pesoc%20000)/20000
pesoc=pesoc%20000
b10=(pesoc-pesoc%10000)/10000
pesoc=pesoc%10000               
b5=(pesoc-pesoc%5000)/5000
pesoc=pesoc%5000           
b2=(pesoc-pesoc%2000)/2000
pesoc=pesoc%2000                        
b1=(pesoc-pesoc%1000)/1000
pesoc=pesoc%1000                           
b05=(pesoc-pesoc%500)/500
pesoc=pesoc%500                               
b02=(pesoc-pesoc%200)/200
pesoc=pesoc%200                                   
b01=(pesoc-pesoc%100)/100
pesoc=pesoc%100                                       
b005=(pesoc-pesoc%50)/50

if b100>0:
    print(b100*100000)  #salida
if b50>0:
    print(b50*50000)  #salida
if b20>0:
    print(b20*20000)  #salida
if b10>0:
    print(b10*10000)  #salida
if b5>0:
    print(b5,5000)  #salida
if b2>0:
    print(b2*2000)  #salida
if b1>0:
    print(b1*1000)  #salida
if b05>0:
    print(b05*500)  #salida
if b02>0:
    print(b02*200)  #salida
if b01>0:
    print(b01*100)  #salida
if b005>0:
    print(b005*50)  #salida