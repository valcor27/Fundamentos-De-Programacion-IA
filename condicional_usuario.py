print("¡Bienvenido al cine!")

# input() detiene el programa y espera a que el usuario escriba algo y presione Enter.
# int() convierte el texto que escribió el usuario en un número entero, para poder hacer operaciones matemáticas con él.
#edad_texto = input("¿Cuántos años tienes? ")
#edad = int(edad_texto) 
edad = int(input("Ingresa tu edad"))
if edad >= 18:
    print("Eres mayor de edad. Puedes entrar a ver la película de terror.")
elif edad >= 13:
    print("Eres adolescente. Puedes ver la película de acción.")
else:
    print("Eres muy pequeño. Te recomendamos la película animada.")