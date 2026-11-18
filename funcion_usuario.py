# 1. Definimos la función llamada 'saludar' que espera un parámetro 'nombre'
def saludar(nombre):
    # 2. Creamos la variable 'mensaje' uniendo el saludo con el parámetro recibido
    mensaje = "¡Hola, " + nombre + "!"
    # 3. Devolvemos la cadena de texto hacia donde fue llamada la función
    return mensaje


# 4. Pedimos al usuario que escriba su nombre y lo guardamos en 'nombre_usuario'
nombre_usuario = input("Escribe tu nombre: ")

# 5. Llamamos a la función pasando la variable leída por teclado
resultado = saludar(nombre_usuario)

# 6. Mostramos el resultado almacenado en la pantalla
print(resultado)