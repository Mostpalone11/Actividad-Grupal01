# Juego de adivinanza de números

import random

# Generar número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Variables para el juego
intentos = 0
adivinado = False

print("Juego de la manzana")
print("He pensado un número entre 1 y 100")
print("¡Trata de adivinarlo!")
print()

# Bucle principal del juego
while not adivinado:
    
    # Pedir número al usuario
    numero_usuario = int(input("Ingresa tu número: "))
    
    # Contar el intento
    intentos = intentos + 1
    
    # Verificar si adivinó
    if numero_usuario == numero_secreto:
        adivinado = True
        print("¡felicidades!")
        print("Adivinaste el número:", numero_secreto)
        print("Lo lograste en", intentos, "intentos")
        
        # Mensaje según la cantidad de intentos
        if intentos <= 5:
            print("¡Excelente! Eres muy bueno adivinando.")
        elif intentos <= 10:
            print("¡Muy bien! Tienes buena intuición.")
        else:
            print("¡Al final lo conseguiste! No te rindas nunca.")
    
    # Si no adivinó, dar pistas
    else:
        if numero_usuario < numero_secreto:
            print("El número es MAYOR que", numero_usuario)
        else:
            print("El número es MENOR que", numero_usuario)
        
        print("Llevas", intentos, "intentos")
        print("¡Sigue intentando!")
        print()

print("¡Gracias por jugar!")