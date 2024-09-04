import numpy as np

# Definir dimensiones
ciudades = ["Esmeraldas", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear una matriz 3D con temperaturas aleatorias
temperaturas = np.random.randint(10, 30, size=(len(ciudades), len(dias_semana), semanas))

# Calcular el promedio de temperaturas para cada ciudad por semana
promedios = np.zeros((len(ciudades), semanas))

for i in range(len(ciudades)):
    for j in range(semanas):
        promedios[i, j] = np.mean(temperaturas[i, :, j])

# Mostrar los promedios de temperaturas
for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for j in range(semanas):
        print(f"  Semana {j+1}: {promedios[i, j]:.2f}°C")