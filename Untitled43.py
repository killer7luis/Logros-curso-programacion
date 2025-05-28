# Crea una lista de números numeros y usa las funciones min() y max() 
#para encontrar el número más pequeño y el más grande. Imprime ambos valores.  



numeros = []
numeros.append(int(input("coloca un numero")))
min_numeros = min(numeros)
max_numeros = max(numeros)

print(min_numeros, max_numeros)