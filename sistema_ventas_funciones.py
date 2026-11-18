# --- FUNCIONES INDEPENDIENTES PARA CADA OPCIÓN ---

def agregar_venta_sabado(ventas):
    nueva_venta = float(input("Ingresa el monto de la nueva venta del Sabado: "))
    ventas.append(nueva_venta)
    print("Venta agregada exitosamente.")
    print("Registro actual:", ventas)

def corregir_dia_venta(ventas):
    if len(ventas) > 0:
        print("Registro actual:", ventas)
        print("Recuerda que los indices empiezan en 0 (0=Lunes, 1=Martes, 2=Miercoles, etc.)")
        indice_a_cambiar = int(input("Escribe el indice del dia que quieres corregir: "))
        
        if 0 <= indice_a_cambiar < len(ventas):
            nuevo_monto = float(input("Ingresa el monto correcto para ese dia: "))
            ventas[indice_a_cambiar] = nuevo_monto 
            print("Dato actualizado correctamente.")
            print("Registro actualizado:", ventas)
        else:
            print("Error: El indice ingresado no existe en la lista.")
    else:
        print("Error: La lista esta vacia. No hay dias para corregir.")

def calcular_ingresos_totales(ventas):
    if len(ventas) > 0:
        total = sum(ventas)
        print("Los ingresos totales de la semana son:", total)
    else:
        print("Error: La lista esta vacia. No hay ventas para sumar.")

def mostrar_mejor_dia(ventas):
    if len(ventas) > 0:
        mejor_venta = max(ventas)
        print("El ingreso del mejor dia de ventas fue:", mejor_venta)
    else:
        print("Error: La lista esta vacia. No se puede calcular el mejor dia.")

def eliminar_por_indice(ventas):
    if len(ventas) > 0:
        print("Registro actual:", ventas)
        indice_a_eliminar = int(input("Escribe el indice del elemento a eliminar (usando pop): "))
        if 0 <= indice_a_eliminar < len(ventas):
            # pop(indice) remueve el elemento en la posición especificada y lo retorna
            eliminado = ventas.pop(indice_a_eliminar)
            print(f"Se elimino el valor {eliminado} del indice {indice_a_eliminar}.")
            print("Registro actualizado:", ventas)
        else:
            print("Error: El indice especificado no existe.")
    else:
        print("Error: La lista esta vacia. No hay elementos para eliminar.")

def eliminar_por_contenido(ventas):
    if len(ventas) > 0:
        print("Registro actual:", ventas)
        monto_a_eliminar = float(input("Escribe el valor/contenido a eliminar (usando remove): "))
        if monto_a_eliminar in ventas:
            # remove(valor) remueve la primera coincidencia del valor en la lista
            ventas.remove(monto_a_eliminar)
            print(f"Se elimino el valor {monto_a_eliminar} de la lista.")
            print("Registro actualizado:", ventas)
        else:
            print("Error: El valor ingresado no se encuentra en la lista.")
    else:
        print("Error: La lista esta vacia. No hay elementos para eliminar.")

# --- FUNCIÓN PRINCIPAL DEL SISTEMA ---

def sistema_ventas():
    ventas_diarias = [1200.0, 1500.0, 900.0, 2100.0, 1800.0]
    
    while True:
        print("\n" + "="*35)
        print("     MENU DE GESTION DE VENTAS")
        print("="*35)
        print("1. Ingresar venta excepcional del Sabado")
        print("2. Corregir un dia de venta")
        print("3. Calcular ingresos totales de la semana")
        print("4. Mostrar el mejor dia de ventas")
        print("5. Eliminar venta por indice (pop)")
        print("6. Eliminar venta por contenido/valor (remove)")
        print("7. Salir del programa")
        print("="*35)
        
        opcion = input("Elige una opcion (1-7): ")
        
        if opcion == '1':
            agregar_venta_sabado(ventas_diarias)
        elif opcion == '2':
            corregir_dia_venta(ventas_diarias)
        elif opcion == '3':
            calcular_ingresos_totales(ventas_diarias)
        elif opcion == '4':
            mostrar_mejor_dia(ventas_diarias)
        elif opcion == '5':
            eliminar_por_indice(ventas_diarias)
        elif opcion == '6':
            eliminar_por_contenido(ventas_diarias)
        elif opcion == '7':
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

# Ejecutamos el programa
sistema_ventas()