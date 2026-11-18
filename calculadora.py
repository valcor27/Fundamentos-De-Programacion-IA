# Entrada de datos
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("\n--- Menú de Opciones ---")
print("1. Sumar")
print("2. Restar")
opcion = int(input("Elige una opción (1 o 2): "))

# Operador lógico 'or' para validar la opción elegida
if opcion == 1 or opcion == 2:
    if opcion == 1:
        resultado = num1 + num2
        print(f"\nEl resultado de la suma es: {resultado}")
    else:
        resultado = num1 - num2
        print(f"\nEl resultado de la resta es: {resultado}")
else:
    print("\nError: Opción inválida. Debes ingresar 1 o 2.")