print("Bienvenido a la aventura de stanley! un dia se encontraba trabajando en su oficina y de repente sus compañeros de trabajo desaparecieron! asi que stanley empezo a buscar por la salida de su oficina!")

inicio = input("Stanley entro a una habitacion con dos puertas abiertas, Stanley entro a la puerta a su IZQUIERDA " )

if inicio == "izquierda":
    iz1 = input("Stanley entro por la puerta a su izquierda y encontro la sala de reuniones vacia, cual podria ser la razon de esto? stanley siguio por varios pasillos hasta encontrar unas escaleras, el fue hacia ARRIBA.")
elif inicio == "derecha":
    iz1 = input("Stanley al parecer no quiso entrar a la puerta a su izquierda y fue a su derecha, seguramente estaba pasando por la sala de descanso, era una sala muy bonita, paso un rato ahi pero siguio adelante, encontrandose con un camino ADELANTE y otro a la IZQUIERDA, la izquierda claramente le devolvia a su camino inicial.")
else:
    print("Al parecer stanley no quiso hacer nada! ni IZQUIERDA o DERECHA, hasta ahi se quedo hasta el fin de los tiempos.")

if iz1 == "adelante":
    print("Al abrir la puerta stanley se da cuenta muy tarde de que no hay un piso detras de ella! stanley cae y muere, fin.")
elif iz1 == "izquierda":
    iz1 = input("Stanley volvio a su camino hacia la libertad en el que encontro 2 escaleras, ARRIBA y ABAJO, stanley sabia que su libertad estaba subiendo arriba")


if iz1 == "arriba":
    print("Stanley subio las escaleras, encontrandose con la oficina de su jefe la cual tambien estaba vacia, por mera casualidad logro encontrar un pasadiso secreto que lo llevo hacia su libertad")
elif iz1 == "abajo":
    print("Stanley se resbala en un charco de agua que estaba en la escalera de abajo, stanley muere! fin.")
else:
    print("Parece que stanley no hizo nada y se quedo en las escaleras, fin.")



