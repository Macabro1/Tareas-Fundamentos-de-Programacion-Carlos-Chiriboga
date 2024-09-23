# Crear un Diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Carlos Chiriboga",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Barcelona"  # Cambiamos Quito por Barcelona

# Agregar una nueva clave-valor al diccionario para "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"  # Actualizamos la profesión

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:  # Si no existe la clave "telefono"
    informacion_personal["telefono"] = "0992879002"  # Agregamos un número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:  # Verificamos si existe la clave "edad"
    del informacion_personal["edad"]  # Eliminamos la clave y su valor

# Imprimir el diccionario final
print(informacion_personal)  # Mostramos el resultado final