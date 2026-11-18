# Definimos los precios de la gasolina
precio_magna = 22.50
precio_premium = 24.20
precio_diesel = 23.60

# 1. Ciclo while para elegir el tipo de gasolina
while True:
    print("\n--- Estación de Gasolina ---")
    print(f"1. Magna (${precio_magna} por litro)")
    print(f"2. Premium (${precio_premium} por litro)")
    print(f"3. Diésel (${precio_diesel} por litro)")

    tipo_gasolina = int(input("Elige el tipo de combustible (1, 2 o 3): "))

    if 1 <= tipo_gasolina <= 3:
        break  # Rompe el ciclo si la opción es correcta
    else:
        print("\nError: Opción inválida. Debes ingresar 1, 2 o 3.")

# Guardamos el precio y el nombre según la elección
if tipo_gasolina == 1:
    precio_actual = precio_magna
    nombre_gasolina = "Magna"
elif tipo_gasolina == 2:
    precio_actual = precio_premium
    nombre_gasolina = "Premium"
elif tipo_gasolina == 3:
    precio_actual = precio_diesel
    nombre_gasolina = "Diésel"

# 2. Ciclo while para elegir la forma de despacho
while True:
    print("\n--- Forma de Despacho ---")
    print("1. Cargar por cantidad de dinero")
    print("2. Cargar por litros (Ver simulación de bomba)")

    metodo_despacho = int(input("Elige cómo deseas cargar (1 o 2): "))

    if 1 <= metodo_despacho <= 2:
        break
    else:
        print("\nError: Opción inválida. Selecciona 1 o 2.")

# 3. Procesar la carga según el método elegido
if metodo_despacho == 1:
    # Opción 1: Carga por dinero (Usa while para validar que el dinero sea positivo)
    while True:
        dinero = float(input("\n¿Cuánto dinero deseas cargar? $"))
        if dinero > 0:
            break
        else:
            print("Error: Debes ingresar una cantidad mayor a cero.")
            
    litros_despachados = dinero / precio_actual
    print(f"\n¡Carga completa! Se despacharon {litros_despachados:.2f} litros de {nombre_gasolina}.")

elif metodo_despacho == 2:
    # Opción 2: Carga por litros (Usa un FOR para simular la bomba despachando)
    while True:
        litros_a_cargar = int(input("\n¿Cuántos litros enteros deseas cargar? "))
        if litros_a_cargar > 0:
            break
        else:
            print("Error: Debes ingresar una cantidad mayor a cero.")
            
    print("\n--- Iniciando bomba de gasolina ---")
    
    # Ciclo for que cuenta desde 1 hasta el número de litros solicitados
    for litro in range(1, litros_a_cargar + 1):
        print(f"Despachando litro... {litro}")
        
    total_a_pagar = litros_a_cargar * precio_actual
    print(f"\n¡Carga completa! Se despacharon {litros_a_cargar} litros de {nombre_gasolina}.")
    print(f"El total a pagar es: ${total_a_pagar:.2f}")

#Escribe un programa en Python que simule el sistema de cobro y despacho de una gasolinera. El programa debe comenzar mostrando un menú con tres tipos de gasolina (Magna, Premium y Diésel) junto con sus precios, utilizando un ciclo `while` para asegurar que el usuario elija una opción válida. Una vez seleccionado el combustible, el sistema debe preguntar si el cliente desea cargar por "cantidad de dinero" o por "cantidad de litros", validando esta elección con otro ciclo `while`. Si el usuario elige por dinero, se le pedirá la cantidad a pagar (validando que sea mayor a cero) y el programa calculará e imprimirá cuántos litros se le despacharon. Si elige por litros, se le pedirá la cantidad deseada y el programa utilizará un ciclo `for` para simular en pantalla la bomba trabajando (imprimiendo "Despachando litro... 1", "Despachando litro... 2", etc.), para finalmente mostrar el total a pagar.