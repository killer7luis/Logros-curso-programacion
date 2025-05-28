#Instrucciones:
#Pregunta al usuario cuántos estudiantes hay en la clase.
#Utiliza un bucle for para solicitar las calificaciones de cada estudiante.
#Almacena todas las calificaciones en una lista.
#Calcula la suma de las calificaciones utilizando la función sum().
#Calcula el promedio dividiendo la suma por el número de estudiantes.
#Encuentra la calificación más alta con max() y la más baja con min().
#Muestra todos los resultados al usuario.

lista = int(input("Coloque el numero de estudiantes"))

calificaciones = []

while len(calificaciones) < lista:
    calificaciones.append(int(input("Coloque una califacion")))


total = sum(calificaciones)
promedio = total / lista
print(f"El promedio es {promedio}")

cal_alta = max(calificaciones)

cal_baja = min(calificaciones)

print(f"La calificación mas alta es {cal_alta} y la calificación mas baja es {cal_baja}")

