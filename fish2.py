# Dados os 3 lados de un triangulo escribe un programa que determine si es equilatero o escaleno

lado1 = int(input("Coloque el primer lado "))

lado2 = int(input("Coloque el segundo lado "))

lado3 = int(input("Coloque el tercer lado "))

if lado1 != lado2 or lado1 != lado3:
    print("Este triangulo es un escaleno")
else:
    lado1 == lado2 and lado1 == lado3
    print("Este triangulo es un equilatero")