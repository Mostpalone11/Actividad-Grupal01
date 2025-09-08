# Calculadora básica en Python

while True: 
    print("\n--- Calculadora ---")

    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Pedimos la operación
    operacion = input("Ingrese la operación (+, -, *, /) o 'salir' para terminar: ")

    # Si el usuario quiere salir
    if operacion == "salir":
        print("¡Hasta luego!")
        break  # Rompe el ciclo y finaliza el programa

    # Realizamos la operación
    if operacion == "+":
        resultado = num1 + num2
        print("El resultado es:", resultado)

    elif operacion == "-":
        resultado = num1 - num2
        print("El resultado es:", resultado)

    elif operacion == "*":
        resultado = num1 * num2
        print("El resultado es:", resultado)

    elif operacion == "/":
        if num2 != 0:  # Verificamos que no sea división entre cero
            resultado = num1 / num2
            print("El resultado es:", resultado)
        else:
            print("Error: No se puede dividir entre cero.")

    else:
        print("Operación no válida. Intente de nuevo.")
