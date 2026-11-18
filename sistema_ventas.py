def sistema_ventas():
    # 1. Creamos la lista inicial con los ingresos de Lunes a Viernes
    ventas_diarias = [1200, 1500, 900, 2100, 1800]
    
    # 2. Mostramos el menú en pantalla
    print("\n" + "="*30)
    print("MENU DE GESTION DE VENTAS")
    print("="*30)
    print("1. Ingresar venta excepcional del Sabado")
    print("2. Corregir un dia de venta")
    print("3. Calcular ingresos totales de la semana")
    print("4. Mostrar el mejor dia de ventas")
    print("="*30)
    
    # 3. Pedimos al usuario que elija una opción
    opcion = input("Elige una opcion (1, 2, 3 o 4): ")
    
    # 4. Evaluamos la opción elegida
    if opcion == '1':
        nueva_venta = float(input("Ingresa el monto de la nueva venta del Sabado: "))
        ventas_diarias.append(nueva_venta)
        print("Venta agregada exitosamente.")
        print("Registro actual:", ventas_diarias)
        
    elif opcion == '2':
        # Verificamos que haya elementos para corregir
        if len(ventas_diarias) > 0:
            print("Registro actual:", ventas_diarias)
            print("Recuerda que los indices empiezan en 0 (0=Lunes, 1=Martes, 2=Miercoles, etc.)")
            
            # Pedimos al usuario que escriba qué índice quiere modificar
            indice_a_cambiar = int(input("Escribe el indice del dia que quieres corregir: "))
            
            # Validamos que el índice ingresado exista dentro del tamaño de la lista
            if indice_a_cambiar >= 0 and indice_a_cambiar < len(ventas_diarias):
                nuevo_monto = float(input("Ingresa el monto correcto para ese dia: "))
                
                # Actualizamos la lista usando la variable que el usuario ingresó
                ventas_diarias[indice_a_cambiar] = nuevo_monto 
                
                print("Dato actualizado correctamente.")
                print("Registro actualizado:", ventas_diarias)
            else:
                print("Error: El indice que escribiste no existe en la lista.")
        else:
            print("Error: La lista esta vacia. No hay dias para corregir.")
            
    elif opcion == '3':
        if len(ventas_diarias) > 0:
            total = sum(ventas_diarias)
            print("Los ingresos totales de la semana son:", total)
        else:
            print("Error: La lista esta vacia. No hay ventas para sumar.")
            
    elif opcion == '4':
        if len(ventas_diarias) > 0:
            mejor_venta = max(ventas_diarias)
            print("El ingreso del mejor dia de ventas fue:", mejor_venta)
        else:
            print("Error: La lista esta vacia. No se puede calcular el mejor dia.")
            
    else:
        print("Opcion no reconocida. Ejecuta el programa de nuevo.")

# Ejecutamos la funcion
sistema_ventas()