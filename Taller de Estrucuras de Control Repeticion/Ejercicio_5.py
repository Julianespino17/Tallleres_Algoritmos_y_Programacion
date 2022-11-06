t=1
sut=0
while sut<1000:
    sut=(t**2+1)/t
    if sut<1000:
        print("El numero puede llegar a ser ",t)  #salidas
    t=t+1