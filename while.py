#Imagina que estás programando un videojuego clásico. 
# El personaje principal empieza con 3 vidas. 
# MIENTRAS el jugador tenga vidas (es decir, mientras sus vidas sean mayores a cero), el juego sigue. 
# Cada vez que choca, pierde una vida. Cuando llega a cero, el juego termina.
vidas = 3

print("¡Comienza el juego!")

# El ciclo se repite MIENTRAS las vidas sean mayores a cero
while vidas > 0:
    print("Tienes", vidas, "vidas. ¡Sigue jugando!")
    
    # Simulamos que el jugador choca y pierde una vida
    vidas = vidas - 1  
    print("¡Ouch! Chocaste y perdiste una vida.")
    print("---")

print("Game Over. Te quedaste sin vidas.")