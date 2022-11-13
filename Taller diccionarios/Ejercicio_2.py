lista={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5} 
R=[]
for i in lista:
    R.append(lista[i])
    k=list(set(R))
print(k)