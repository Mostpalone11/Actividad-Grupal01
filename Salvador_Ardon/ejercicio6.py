import random

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("adivina el número")
print("Estoy pensando en un número entre 1 y 100.")

# Bucle while
while not adivinado:
    try:
        
        intento_usuario = int(input("Adivina el número: "))
        intentos += 1

        # Compara el intento con el número secreto
        if intento_usuario < numero_secreto:
            print("Mayor") #pista
        elif intento_usuario > numero_secreto:
            print("Menor") #pista
        else:
            adivinado = True  # Se adivinó el número
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
