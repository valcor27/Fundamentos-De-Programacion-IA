# 1. Creamos un arreglo con 5 números (temperaturas de Lunes a Viernes)
temperaturas = [22, 24, 19, 21, 25]

# 2. Podemos saber cuántos elementos tiene la lista usando la función len() (length = longitud)
cantidad_dias = len(temperaturas)
print("Días registrados:", cantidad_dias)

# 3. Mostramos las temperaturas una por una usando un ciclo 'for'
# Esto recorrerá la lista de principio a fin automáticamente.
print("--- Temperaturas de la semana ---")
for temp in temperaturas:
    print(temp, "grados")

# 4. Las listas de Python nos permiten hacer cálculos rápidos.
# Por ejemplo, encontrar la temperatura más alta usando max()
temperatura_maxima = max(temperaturas)
print("\nLa temperatura más alta fue:", temperatura_maxima)

# 5. O sumar todos los elementos para calcular un promedio
suma_total = sum(temperaturas)
promedio = suma_total / cantidad_dias
print("La temperatura promedio fue:", promedio)