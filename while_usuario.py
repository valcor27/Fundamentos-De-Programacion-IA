print("¡Estás atrapado en el bucle!")
respuesta = ""
while respuesta != "magia":
    # Volvemos a preguntar DENTRO del ciclo para darle otra oportunidad
    respuesta = input("Adivina la palabra secreta para poder salir: ")
    
    if respuesta != "magia":
        print("Incorrecto. Intenta de nuevo.")

print("¡Felicidades! Escribiste 'magia' y lograste escapar del bucle.")