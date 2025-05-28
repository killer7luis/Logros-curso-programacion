# 5. ¿Fin de semana o día de semana?: Pide al usuario que ingrese un día de la semana 
# (por ejemplo, "lunes", "sábado"). El programa debe indicar si es un día de semana o fin de semana.

dia = input("Por favor coloca un dia de la semana")

if dia == "sabado" or dia == "domingo":
    print("Es un fin de semana")
elif dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes":
    print("No es un fin de semana")
else:
    print("Eso no es un dia")