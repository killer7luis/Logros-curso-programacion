#aAsignación
#Para este proyecto, el usuario recibirá un menú y tendrá la capacidad de elegir elementos del menú.
#  Las opciones del menú son las siguientes:

#Agregar un nuevo elemento

#Mostrar el contenido de la cesta de la compra

#Eliminar un elemento 

#Calcular el total 

#Renunciar

#Cuando el usuario elige una de estas opciones, el programa debe realizar la acción adecuada.
#  A continuación, el programa debería mostrarles el menú de nuevo y permitirles elegir otra opción.
#  Debe continuar ejecutándose hasta que el usuario elija la opción de salir.




menuact = 1

objetos = [("Leche", 50), ("Arroz", 100), ("Carne", 200), ("Papa", 10)]

listcomp = []

while menuact == 1:
    print("----------------------")
    print("AÑADIR - Agregar un nuevo elemento")
    print("")
    print ("MOSTRAR - Mostrar el contenido de la lista")
    print("")
    print("ELIMINAR - Eliminar un elemento")
    print("")
    print("TOTAL - Calcular el total")
    print("")
    print("SALIR - terminar programa")
    print("----------------------")

    menu = input("Por favor elija una opcion, coloque SALIR para terminar el programa: ")
    if menu == "SALIR":
        break
    elif menu == "AÑADIR":
        menuact = 0
        print("----------------------")
        print("LECHE,50")
        print("")
        print("ARROZ, 100")
        print("")
        print("CARNE, 200")
        print("")
        print("PAPA, 10")
        print("----------------------")
        compra = input("Por favor escriba el nombre del producto que quiera añadir a su lista: ")
        if compra == "LECHE":
            listcomp.append(objetos[0])
            menuact = 1
        elif compra == "ARROZ":
            listcomp.append(objetos[1])
            menuact = 1
        elif compra == "CARNE":
            listcomp.append(objetos[2])
            menuact = 1
        elif compra == "PAPA":
            listcomp.append(objetos[3])
            menuact = 1
        else:
            menuact = 1
    elif menu == "MOSTRAR":
        print(listcomp)

    elif menu == "ELIMINAR":
        menuact = 0
        print(listcomp)
        borrar = input("Por favor coloque el nombre de el objeto que quiera eliminar: ")
        if borrar == "LECHE":
            listcomp.remove(("Leche", 50))
            menuact = 1
        elif borrar == "ARROZ":
            listcomp.remove(("Arroz", 100))
            menuact = 1
        elif borrar == "CARNE":
            listcomp.remove(("Carne", 200))
            menuact = 1
        elif borrar == "PAPA":
            listcomp.remove(("Papa", 10))
            menuact = 1
        else:
            menuact = 1

    elif menu == "TOTAL":
        tot = input()