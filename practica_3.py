# ==========================================
# DEFINICIÓN DE FUNCIONES DEL GRAFO
# ==========================================

def mostrar_red(grafo):
    print("\n--- RED SOCIAL ACTUAL ---")
    if len(grafo) == 0:
        print("La red esta vacia.")
    else:
        for persona in grafo:
            amigos = grafo[persona]
            print("-", persona, "tiene", len(amigos), "amigos:", amigos)

def agregar_persona(grafo, nueva_persona):
    if nueva_persona not in grafo:
        grafo[nueva_persona] = [] 
        print("Se agrego a", nueva_persona, "exitosamente.")
    else:
        print("Error:", nueva_persona, "ya existe en la red.")

def agregar_amistad(grafo, persona1, persona2):
    if persona1 in grafo and persona2 in grafo:
        if persona2 not in grafo[persona1]:
            grafo[persona1].append(persona2)
            grafo[persona2].append(persona1)
            print("Exito:", persona1, "y", persona2, "ahora son amigos.")
        else:
            print("Aviso: Ya eran amigos anteriormente.")
    else:
        print("Error: Ambas personas deben estar registradas primero.")

def eliminar_amistad(grafo, persona1, persona2):
    if persona1 in grafo and persona2 in grafo:
        if persona2 in grafo[persona1]:
            grafo[persona1].remove(persona2)
            grafo[persona2].remove(persona1)
            print("Exito:", persona1, "y", persona2, "ya no son amigos.")
        else:
            print("Aviso: Estas personas no son amigos actualmente.")
    else:
        print("Error: Alguna de las personas no existe en la red.")

def eliminar_persona(grafo, persona):
    if persona in grafo:
        # Eliminar de las listas de amigos de los demas
        for amigo in grafo[persona]:
            grafo[amigo].remove(persona)
        
        # Eliminar del diccionario
        del grafo[persona]
        print("Exito:", persona, "ha sido eliminado de la red.")
    else:
        print("Error:", persona, "no existe en la red.")

def buscar_amigos(grafo, persona):
    if persona in grafo:
        print("\nLos amigos de", persona, "son:", grafo[persona])
    else:
        print("Error:", persona, "no esta en la red.")

def persona_mas_amigos(grafo):
    if len(grafo) == 0:
        print("La red esta vacia, no hay datos para calcular.")
        return

    max_amigos = -1
    nombre_mayor = ""

    for persona in grafo:
        cantidad = len(grafo[persona])
        if cantidad > max_amigos:
            max_amigos = cantidad
            nombre_mayor = persona

    print("\nLa persona con MAS amigos (nodo de mayor grado) es:", nombre_mayor, "con", max_amigos, "amigos.")

def persona_menos_amigos(grafo):
    if len(grafo) == 0:
        print("La red esta vacia, no hay datos para calcular.")
        return

    # Usamos un numero grande inicial para poder encontrar el menor
    min_amigos = 999999
    nombre_menor = ""

    for persona in grafo:
        cantidad = len(grafo[persona])
        if cantidad < min_amigos:
            min_amigos = cantidad
            nombre_menor = persona

    print("\nLa persona con MENOS amigos (nodo de menor grado) es:", nombre_menor, "con", min_amigos, "amigos.")


# ==========================================
# BLOQUE PRINCIPAL (MENÚ INTERACTIVO)
# ==========================================

mi_red = {}

while True:
    print("\n==============================")
    print("   MENU DE RED SOCIAL")
    print("==============================")
    print("1. Mostrar toda la red")
    print("2. Agregar nueva persona")
    print("3. Crear amistad (Agregar arista)")
    print("4. Eliminar amistad (Eliminar arista)")
    print("5. Eliminar persona (Eliminar nodo)")
    print("6. Ver amigos de alguien")
    print("7. Persona con mas amigos")
    print("8. Persona con menos amigos")
    print("9. Salir")
    print("==============================")
    
    opcion = input("Elige una opcion (1-9): ")
    
    if opcion == "1":
        mostrar_red(mi_red)
        
    elif opcion == "2":
        nombre = input("Ingresa el nombre de la nueva persona: ")
        agregar_persona(mi_red, nombre)
        
    elif opcion == "3":
        p1 = input("Ingresa el nombre de la primera persona: ")
        p2 = input("Ingresa el nombre de la segunda persona: ")
        if p1 != p2:
            agregar_amistad(mi_red, p1, p2)
        else:
            print("Error: Una persona no puede ser amiga de si misma.")
            
    elif opcion == "4":
        p1 = input("Ingresa el nombre de la primera persona: ")
        p2 = input("Ingresa el nombre de la segunda persona: ")
        eliminar_amistad(mi_red, p1, p2)
        
    elif opcion == "5":
        nombre = input("Ingresa el nombre de la persona a eliminar: ")
        eliminar_persona(mi_red, nombre)
        
    elif opcion == "6":
        nombre = input("Ingresa el nombre de la persona a buscar: ")
        buscar_amigos(mi_red, nombre)
        
    elif opcion == "7":
        persona_mas_amigos(mi_red)

    elif opcion == "8":
        persona_menos_amigos(mi_red)

    elif opcion == "9":
        print("Saliendo del programa...")
        break 
        
    else:
        print("Opcion no valida. Por favor ingresa un numero del 1 al 9.")