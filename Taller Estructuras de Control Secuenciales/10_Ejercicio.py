chelines_austriacos=float(input("Ingrese la cantidad de chelines austriacos: "))
dragmas_griegos=float(input("Ingrese la cantidad de dragmas griegos: "))
pesetas=float(input("Ingrese la cantidad de pesetas: "))


Chelines_austriacos_pesetas=chelines_austriacos*9.56
Dragmas_griegos_francos_franceses=((chelines_austriacos*0.956)/20.110)
Pesetas_dolares=pesetas/122.499
Pesetas_liras_intalianas=pesetas/0.092289


print(chelines_austriacos, " chelines equivalen a", Chelines_austriacos_pesetas, " pesetas")
print(dragmas_griegos, " dragmas griegos equivalen a", Dragmas_griegos_francos_franceses, " francos franceses")
print(pesetas, " pesetas equivalen a", Pesetas_dolares, " dolares y ", Pesetas_liras_intalianas, " liras italianas")