# Entrada de datos
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Ciclo while para pedir la opción hasta que sea correcta
while True:
    print("\n--- Menú de Opciones ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Elige una opción (1, 2, 3 o 4): "))

    # Verificamos si la opción es válida
    if 1 <= opcion <= 4:
        break  # Rompe el ciclo while y continúa con el programa
    else:
        print("\nError: Opción inválida. Debes ingresar un número del 1 al 4.")

# Se ejecuta solo cuando el usuario ingresa 1 o 2
if opcion == 1:
    resultado = num1 + num2
    print(f"\nEl resultado de la suma es: {resultado}")
elif opcion == 2:
    resultado = num1 - num2
    print(f"\nEl resultado de la resta es: {resultado}")
elif opcion == 3:
    resultado = num1 * num2
    print(f"\nEl resultado de la multiplicación es: {resultado}")
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nEl resultado de la división es: {resultado}")
    else:
        print("\nError: No se puede dividir entre cero.")