import random
import time
import os

def generar_numeros_aleatorios(cantidad):
    return [random.randint(0, 9) for _ in range(cantidad)]

def mostrar_numeros(numeros, tiempo_mostrar):
    for numero in numeros:
        print(numero, end=' ', flush=True)
    time.sleep(tiempo_mostrar)
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla

def pedir_respuesta(numeros):
    print("Introduce los números en el orden que los viste, separados por espacios:")
    respuesta = list(map(int, input().split()))
    if respuesta == numeros:
        print("¡Correcto! Has memorizado los números correctamente.")
    else:
        print(f"Incorrecto. La secuencia correcta era: {' '.join(map(str, numeros))}")

def main():
    cantidad = int(input("¿Cuántos números deseas memorizar? "))
    tiempo_mostrar = int(input("¿Cuánto tiempo (en segundos) deseas que se muestren los números? "))

    numeros = generar_numeros_aleatorios(cantidad)
    mostrar_numeros(numeros, tiempo_mostrar)

    time.sleep(1)  # Esperar 1 segundo en blanco
    pedir_respuesta(numeros)

if __name__ == "__main__":
    main()
