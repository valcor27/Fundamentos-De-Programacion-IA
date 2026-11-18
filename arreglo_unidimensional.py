# 1. Creamos el arreglo (lista) con 3 elementos iniciales.
mochila = ["Espada", "Escudo", "Poción", "Poción"]

# 2. Imprimimos todo el inventario para ver qué hay dentro.
#print("Inventario inicial:", mochila)

# 3. Accedemos a un elemento específico usando su índice (posición).
# ¡Ojo! En programación, empezamos a contar desde el CERO.
#print("El primer objeto es:", mochila[0])  # Imprime "Espada"
#print("El tercer objeto es:", mochila[2])  # Imprime "Poción"

# 4. Agregamos un nuevo objeto al final del arreglo usando .append()
#mochila.append("Mapa")
#print("Encontramos un mapa:", mochila)

# 5. Modificamos un objeto que ya existe. 
# Usamos la poción (posición 2) y la cambiamos por un frasco vacío.
#mochila[2] = "Frasco vacío"
#print("Después de usar la poción:", mochila)

#elimina el indice
mochila.pop(0)
print("Después de eliminar el primer elemento:", mochila)

#elimina la primera aparición del valor
mochila.remove('Poción')
print("Despues de eliminar Poción", mochila)

