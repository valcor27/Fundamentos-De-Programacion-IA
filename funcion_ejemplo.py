# 1. Definimos la función llamada 'saludar' que recibe un parámetro 'nombre'
def saludar(nombre):
    # 2. Creamos la variable 'mensaje' uniendo el saludo con el nombre recibido
    mensaje = "¡Hola, " + nombre + "!"
    # 3. Devolvemos la cadena de texto hacia donde fue llamada la función
    return mensaje


# 4. Llamamos a la función pasando "Ana" y guardamos la respuesta en 'resultado'
resultado = saludar("Ana")
resultado_dos = saludar("Erick")
resultado_tres = saludar("Ale")

# 5. Mostramos el resultado almacenado en la pantalla
print(resultado)
print(resultado_dos)
print(resultado_tres)