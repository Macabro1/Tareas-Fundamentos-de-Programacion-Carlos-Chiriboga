def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento dado el monto total y el porcentaje de descuento.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto es 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Llamadas a la función
monto_1 = 1500  # Ejemplo de monto total
porcentaje_1 = 15  # Ejemplo de porcentaje de descuento

# Primera llamada: Solo monto total, porcentaje de descuento por defecto (10%)
descuento_1 = calcular_descuento(monto_1)
monto_final_1 = monto_1 - descuento_1

# Segunda llamada: Monto total y porcentaje de descuento especificado (15%)
descuento_2 = calcular_descuento(monto_1, porcentaje_1)
monto_final_2 = monto_1 - descuento_2

# Mostrar resultados
print(f"Para un monto total de ${monto_1} con descuento por defecto:")
print(f"Descuento calculado: ${descuento_1:.2f}")
print(f"Monto final a pagar: ${monto_final_1:.2f}")

print("\nPara un monto total de ${monto_1} con un descuento del 15%:")
print(f"Descuento calculado: ${descuento_2:.2f}")
print(f"Monto final a pagar: ${monto_final_2:.2f}")