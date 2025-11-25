def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    Autor: Luis
    """
    if not numeros:
        return 0
    
    suma_total = sum(numeros)
    cantidad = len(numeros)
    
    return suma_total / cantidad


# Prueba de la función
lista = [10, 20, 30]
print("Promedio:", calcular_promedio(lista))
# Salida esperada: Promedio: 20.0