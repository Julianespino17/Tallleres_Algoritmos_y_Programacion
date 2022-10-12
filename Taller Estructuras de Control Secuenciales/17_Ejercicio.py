#entrada
presupuesto_anual=float(input("Ingrese el presupuesto anual: "))
#caja negra
presupuesto_ginecologia=(presupuesto_anual)*0.40
presupuesto_traumatologia=(presupuesto_anual)*0.30
presupuesto_pediatria=(presupuesto_anual)*0.30
#salida
print("Ginecologia recibira un presupuesto de: ",presupuesto_ginecologia)
print("Traumatologia recibira un presupuesto de: ",presupuesto_traumatologia)
print("Pediatria recibira un presupuesto de:", presupuesto_pediatria)
