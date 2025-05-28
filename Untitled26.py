# Información de un usuario
usuario = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Maracaibo"
}

# Acceder a un valor usando su clave
print(usuario["nombre"])  # Salida: Carlos

# Modificar un valor
usuario["edad"] = 31
print(usuario) # {'nombre': 'Carlos', 'edad': 31, 'ciudad': 'Maracaibo'}

# Añadir un nuevo par clave-valor
usuario["profesion"] = "Ingeniero"
print(usuario)