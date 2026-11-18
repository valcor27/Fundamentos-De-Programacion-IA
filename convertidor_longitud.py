# Ciclo while para pedir los metros hasta que sea un valor válido (no negativo)
while True:
    metros = float(input("Ingresa la cantidad en metros: "))
    
    # Verificamos si el valor es correcto (mayor o igual a cero)
    if metros >= 0:
        break  # Rompe el ciclo while y continúa con el programa
    else:
        print("\nError: La distancia no puede ser negativa. Intenta de nuevo.\n")

# Ciclo while para pedir la opción hasta que sea correcta
while True:
    print("\n--- Menú de Conversiones ---")
    print("1. Convertir a Kilómetros")
    print("2. Convertir a Centímetros")
    print("3. Convertir a Millas")
    print("4. Convertir a Pies")

    opcion = int(input("Elige una opción (1, 2, 3 o 4): "))

    # Verificamos si la opción es válida
    if 1 <= opcion <= 4:
        break  # Rompe el ciclo while y continúa con el programa
    else:
        print("\nError: Opción inválida. Debes ingresar un número del 1 al 4.")

# Se ejecuta solo cuando el usuario ingresó una opción válida
if opcion == 1:
    resultado = metros / 1000
    print(f"\n{metros} metros equivalen a: {resultado} km")
elif opcion == 2:
    resultado = metros * 100
    print(f"\n{metros} metros equivalen a: {resultado} cm")
elif opcion == 3:
    resultado = metros / 1609.34
    print(f"\n{metros} metros equivalen a: {resultado} millas")
elif opcion == 4:
    resultado = metros * 3.28084
    print(f"\n{metros} metros equivalen a: {resultado} pies")