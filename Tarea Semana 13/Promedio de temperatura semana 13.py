def calcular_promedio_temperaturas(temperaturas, nombres_ciudades):
    """
    Calcula el promedio de temperaturas para cada ciudad durante un período de tiempo.

    :param temperaturas: Lista 3D con datos de temperaturas.
                         La estructura es [ciudades][semanas][días]
    :param nombres_ciudades: Lista con los nombres de las ciudades.
    :return: None
    """
    # Asegurarse de que las dimensiones coinciden
    assert len(temperaturas) == len(
        nombres_ciudades), "El número de ciudades no coincide con el número de nombres proporcionados."

    for ciudad_index, ciudad in enumerate(temperaturas):
        ciudad_nombre = nombres_ciudades[ciudad_index]
        suma_total = 0
        conteo_total = 0

        print(f"Ciudad: {ciudad_nombre}")

        for semana_index, semana in enumerate(ciudad):
            suma_semana = sum(dia['temp'] for dia in semana)
            conteo_semana = len(semana)
            promedio_semana = suma_semana / conteo_semana

            suma_total += suma_semana
            conteo_total += conteo_semana

            print(f"  Semana {semana_index + 1}: Promedio de Temperatura = {promedio_semana:.2f}°C")

        promedio_total = suma_total / conteo_total
        print(f"  Promedio General: {promedio_total:.2f}°C\n")


# Datos de ejemplo
temperaturas = [
    [  # Ciudad 1: Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 20}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ]
    ],
    [  # Ciudad 2: Guayaquil
        [  # Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [  # Ciudad 3: Cuenca
        [  # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 21}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 22}
        ]
    ]
]

# Nombres de las ciudades
nombres_ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Llamar a la función para calcular y mostrar los promedios
calcular_promedio_temperaturas(temperaturas, nombres_ciudades)