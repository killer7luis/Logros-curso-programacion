# Escribe un programa  que saque el descuento del monto de la compra de
# un cliente vip de una tienda. Con Condicionales

precio = int(input("Coloca precio"))

descuento = 15 / precio * 100

total = precio - descuento

vip = input("Es un VIP?")

if vip == "si":
    print(total)
else:
    print(precio)

