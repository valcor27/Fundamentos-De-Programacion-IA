limite_tanque = int(input("¿Con cuántos pesos se llena tu tanque?: $"))
pesos_cargados = 0

print("\n --- Llenando tanque ---")

#El ciclo while se ejecuta MIENTRAS no hayamos alcanzado el límite
while pesos_cargados < limite_tanque:
    pesos_cargados += 20 #suma de 20 en 20 en pesos al acumulador

    #si nos pasamos del límite, ajustamos al monto exacto
    if pesos_cargados > limite_tanque:
        pesos_cargados = limite_tanque

    print(f"Cargando.... Van ${pesos_cargados} de ${limite_tanque} pesos")
print("Tanque lleno")