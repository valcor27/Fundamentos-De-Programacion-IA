#funcion calcular_promedio
def calcular_promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3)/3
    return promedio

#Programa principal
print("---- Calculadora de promedio----")

n1 = float(input("Ingresa la primera calificación: "))
n2 = float(input("Ingresa la segunda calificación: "))
n3 = float(input("Ingresa la tercera calificación: "))

resultado = calcular_promedio(n1, n2, n3)

print(f"\nTu promedio final es: {resultado}")

if resultado >= 70:
    print("Felicidades pasaste programación")
else:
    print("Reprobaste, sigue estudiando")
