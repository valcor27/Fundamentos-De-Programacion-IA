# 1. Definimos la clase 'Perro'
class Perro:

    # 2. Definimos el método 'saludar' que recibe 'self' y el parámetro 'persona'
    def saludar(self, persona):
        # 3. Devuelve una frase combinando la acción del perro con el nombre ingresado
        return "El perro mueve la cola y saluda a " + persona


# 4. Creamos una instancia u objeto de la clase Perro llamado 'mi_perro'
mi_perro = Perro()

# 5. Leemos por teclado el nombre de la persona que el perro va a saludar
persona_ingresada = input("¿A quién debe saludar el perro?: ")

# 6. Invocamos el método '.saludar()' directamente sobre el objeto 'mi_perro'
accion = mi_perro.saludar(persona_ingresada)

# 7. Imprimimos el texto devuelto por el método
print(accion)