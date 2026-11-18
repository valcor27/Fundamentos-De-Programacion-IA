#Pide al usuario que escriba su nombre o cualquier palabra. 
# El programa deberá tomar esa palabra y deletrearla, imprimiendo una letra a la vez hacia abajo.

# Guardamos lo que el usuario escriba directamente en la variable 'palabra'
palabra = input("Escribe tu nombre o una palabra: ")

print("Deletreando tu palabra...")

# La variable 'letra' tomará un carácter distinto en cada vuelta.
for letra in palabra:
    print(letra)

print("¡Terminamos de deletrear!")