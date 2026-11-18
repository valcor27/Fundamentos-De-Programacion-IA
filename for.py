#Quieres que el programa pase lista saludando a cada uno por su nombre, uno por uno, hasta terminar.
# Tenemos una lista con tres nombres
alumnos = ["Ana", "Luis", "Carlos"]

print("Iniciando pase de lista:")

# El bucle for toma un nombre a la vez
for persona in alumnos:
    print("¡Hola " + persona + "!")

print("Pase de lista terminado.")