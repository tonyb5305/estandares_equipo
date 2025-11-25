def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio final luego de aplicar un descuento.
    Autor: Keiner
    """
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final


# Prueba
print("Precio final:", calcular_descuento(100000, 15))
# Salida esperada: Precio final: 85000.0