# ==========================================
# 1. CICLO FOR (Carga por pesos)
# ==========================================

monto_deseado = int(input("¿Cuántos pesos deseas cargar?: $"))
acumulado = 0

print("\n--- Iniciando carga ---")

for incremento in range(10, monto_deseado + 1, 10):
    acumulado = incremento  # acumulador
    print(f"Cargando... Van ${acumulado} pesos")

print(f"¡Carga completada! Total: ${acumulado} pesos.\n")