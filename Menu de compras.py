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

objetos = ["LECHE", "ARROZ", "CARNE", "PAPA"]

precios = [50,100, 200, 10]

pricecomp = []

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
            pricecomp.append(precios[0])
            listcomp.append(objetos[0])
            menuact = 1
        elif compra == "ARROZ":
            pricecomp.append(precios[1])
            listcomp.append(objetos[1])
            menuact = 1
        elif compra == "CARNE":
            pricecomp.append(precios[2])
            listcomp.append(objetos[2])
            menuact = 1
        elif compra == "PAPA":
            pricecomp.append(precios[3])
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
            listcomp.remove(0)
            pricecomp.remove(0)
            menuact = 1
        elif borrar == "ARROZ":
            listcomp.remove(1)
            pricecomp.remove(1)
            menuact = 1
        elif borrar == "CARNE":
            listcomp.remove(2)
            pricecomp.remove(2)
            menuact = 1
        elif borrar == "PAPA":
            listcomp.remove(3)
            pricecomp.remove(3)
            menuact = 1
        else:
            menuact = 1

    elif menu == "TOTAL":
        total = sum(pricecomp)
        print(total)