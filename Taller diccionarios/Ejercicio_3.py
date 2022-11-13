usuarios ={
    "iperurena":{
        "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    },
}
intentos=1
for i in usuarios:
    N= input("Usuario:")
    P= input("contraseña:")
    if N in usuarios and P== usuarios[N]["password"]:
        nombre=usuarios[N]["nombre"]
        apellido=usuarios[N]["apellido"]
        print(nombre)
        print(apellido)
        break
    if i==3:
        print("Sus intentos se acabaron ")
        break
    else:
        print("Intentelo de nuevo")