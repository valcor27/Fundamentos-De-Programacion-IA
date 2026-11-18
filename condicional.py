#Escribe un programa que evalúe el nivel de batería del dron. 
# Si la batería es mayor o igual a 80%, imprime "Estado óptimo". 
# Si está entre 20% y 79%, imprime "Estado normal". 
# Si es menor a 20%, imprime "Alerta: Regreso a la base

# Definimos el nivel de batería actual del dron
nivel_bateria = 100

if nivel_bateria >= 80:
    print("Estado óptimo: El dron puede continuar la misión.")
elif nivel_bateria >= 20:
    print("Estado normal: Monitoreando consumo de energía.")
else:
    print("Alerta roja: Batería crítica. Iniciando protocolo de regreso a la base.")