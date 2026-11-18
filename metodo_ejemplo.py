# 1. Definimos la clase 'Perro' (sirve como plantilla para crear objetos de tipo perro)
class Perro:

    # 2. Definimos el método 'ladrar'. 'self' representa al objeto concreto que lo ejecute
    def ladrar(self):
        # 3. El método devuelve el texto de la acción
        return "¡Guau, guau!"


# 4. Creamos una instancia u objeto real de la clase Perro llamado 'mi_perro'
mi_perro = Perro()

# 5. Invocamos el método '.ladrar()' directamente sobre el objeto 'mi_perro'
sonido = mi_perro.ladrar()

# 6. Imprimimos el resultado devuelto por el método
print(sonido)