#Login Simple: Escribe un programa que simule un inicio de sesión. 
#Pide un nombre de usuario y una contraseña. El acceso solo se concede 
#si el usuario es "admin" y la contraseña es "1234".

user = "admin"

password = 1234

login = input("Ingresa tu usuario")

loginp = int(input("Ingresa tu contraseña"))

if login == "admin" and loginp == 1234:
    print("Acceso establecido, bienvenido al servidor")
else:
    print("Acceso denegado")