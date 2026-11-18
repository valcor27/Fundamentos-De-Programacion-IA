# 1. Definición del grafo usando un diccionario
# Cada nombre es un "nodo" y la lista contiene las personas con las que está conectado.
red_social = {
    "Ana": ["Luis", "Juan", "Marta"],
    "Luis": ["Ana", "Pedro"],
    "Juan": ["Ana"],
    "Marta": ["Ana", "Pedro"],
    "Pedro": ["Luis", "Marta"]
}

# 2. Mostrar todas las conexiones (Recorrer el grafo)
print("--- RED SOCIAL ACTUAL ---")
for persona in red_social:
    amigos = red_social[persona]
    # Usamos len() para saber cuántos amigos tiene
    print(persona, "tiene", len(amigos), "amigos:", amigos)

# 3. Buscar las conexiones de un nodo específico
print("\n--- BUSCAR AMIGOS ---")
persona_buscada = "Luis"

if persona_buscada in red_social:
    print("Los amigos de", persona_buscada, "son:", red_social[persona_buscada])
else:
    print(persona_buscada, "no está en la red social.")

# 4. Agregar un nuevo nodo (Una nueva persona a la red)
print("\n--- AGREGAR NUEVA PERSONA ---")
red_social["Carlos"] = [] # Carlos entra a la red sin amigos al principio
print("Se agregó a Carlos:", red_social)

# 5. Agregar una nueva arista (Conectar a dos personas)
print("\n--- NUEVA AMISTAD ---")
print("Haciendo amigos a Carlos y Juan...")

# Como la amistad es de dos vías (Grafo no dirigido), agregamos a ambos
red_social["Carlos"].append("Juan")
red_social["Juan"].append("Carlos")

print("Amigos de Carlos ahora:", red_social["Carlos"])
print("Amigos de Juan ahora:", red_social["Juan"])