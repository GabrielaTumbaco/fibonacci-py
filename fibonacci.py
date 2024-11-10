import random

def generar_fibonacci_aleatorio(longitud):
    # Los dos primeros números de la secuencia de Fibonacci son aleatorios
    a = random.randint(1, 10)  # Primer número aleatorio
    b = random.randint(1, 10)  # Segundo número aleatorio

    print("Secuencia Fibonacci Aleatoria:")

    # Imprimir los dos primeros números
    print(a, b, end=" ")

    # Generar el resto de la secuencia de Fibonacci
    for _ in range(3, longitud + 1):
        siguiente = a + b
        print(siguiente, end=" ")

        # Actualizar los valores de a y b
        a = b
        b = siguiente

    print()  # Para añadir una nueva línea después de la secuencia

# Generar una secuencia de Fibonacci aleatoria con longitud aleatoria (entre 5 y 14)
longitud = random.randint(5, 14)
generar_fibonacci_aleatorio(longitud)

