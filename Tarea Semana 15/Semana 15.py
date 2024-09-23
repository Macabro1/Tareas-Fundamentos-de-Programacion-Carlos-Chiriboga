# Crear un Diccionario
informacion_personal = {
    "nombre": "Carlos Chiriboga",
    "edad": 45,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
# Accediendo al valor de la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificando el valor de "ciudad"
informacion_personal["ciudad"] = "Barcelona"

# Agregando una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Arquitecto"

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "593-992-79002"

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el Diccionario Final
print(informacion_personal)