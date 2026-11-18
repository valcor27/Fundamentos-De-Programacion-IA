# 1. Función para mostrar todo el grafo
def mostrar_red(grafo):
    print("\n--- RED SOCIAL ACTUAL ---")
    for persona in grafo:
        amigos = grafo[persona]
        print(persona, "tiene", len(amigos), "amigos:", amigos)

# 2. Función para buscar a una persona
def buscar_amigos(grafo, persona):
    print("\n--- BUSCANDO A:", persona, "---")
    if persona in grafo:
        print("Los amigos de", persona, "son:", grafo[persona])
    else:
        print("La persona", persona, "no está en la red social.")

# 3. Función para agregar un nuevo nodo (persona)
def agregar_persona(grafo, nueva_persona):
    print("\n--- AGREGANDO PERSONA ---")
    if nueva_persona not in grafo:
        grafo[nueva_persona] = [] # Se crea con una lista vacía de amigos
        print("Se agregó a", nueva_persona, "exitosamente.")
    else:
        print("Error:", nueva_persona, "ya existe en la red.")

# 4. Función para agregar una arista (amistad)
def agregar_amistad(grafo, persona1, persona2):
    print("\n--- NUEVA AMISTAD ---")
    # Primero verificamos que ambas personas existan en el diccionario
    if persona1 in grafo and persona2 in grafo:
        grafo[persona1].append(persona2)
        grafo[persona2].append(persona1)
        print("¡", persona1, "y", persona2, "ahora son amigos!")
    else:
        print("Error: Ambas personas deben estar registradas para ser amigos.")


# ==========================================
# BLOQUE PRINCIPAL (Aquí usamos las funciones)
# ==========================================

# Nuestro grafo inicial
red_social = {
    "Ana": ["Luis", "Juan", "Marta"],
    "Luis": ["Ana", "Pedro"],
    "Juan": ["Ana"],
    "Marta": ["Ana", "Pedro"],
    "Pedro": ["Luis", "Marta"]
}

# Probamos las funciones paso a paso
mostrar_red(red_social)

buscar_amigos(red_social, "Luis")
buscar_amigos(red_social, "Roberto") # Probamos con alguien que no existe

agregar_persona(red_social, "Carlos")

agregar_amistad(red_social, "Carlos", "Juan")

# Mostramos la red final para comprobar los cambios
mostrar_red(red_social)