# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado my_notes.txt y escribimos notas en él
with open('my_notes.txt', 'w') as file:  # 'w' indica que vamos a escribir en el archivo
    file.write("Nota 1: Recuerda grabar en GitHub.\n")  # Escribimos la primera línea
    file.write("Nota 2: Estudiar para el examen de Fundamentos de Programación.\n")  # Escribimos la segunda línea
    file.write("Nota 3: Llamar al grupo para el proyecto.\n")  # Escribimos la tercera línea

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt y leemos su contenido línea por línea
with open('my_notes.txt', 'r') as file:  # 'r' indica que vamos a leer el archivo
    # Leemos cada línea y la mostramos en la consola
    for line in file:  # Iteramos sobre cada línea del archivo
        print(line.strip())  # Mostramos la línea, eliminando el salto de línea al final

# No es necesario cerrar el archivo manualmente al usar 'with',
# ya que se cierra automáticamente al salir del bloque