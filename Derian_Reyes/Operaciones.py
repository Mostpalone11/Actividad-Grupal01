while True:
    # Solicitar los números y la operación
    num1 = float(input("Ingresa el primer número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))
    
    # Realizar la operación seleccionada
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        # Verificar división entre cero
        if num2 == 0:
            print("Error: No se puede dividir entre cero")
            continue
        resultado = num1 / num2
    else:
        print("Operación no válida")
        continue
    
    # Mostrar el resultado
    print(f"Resultado: {resultado}")
    
    # Preguntar si desea continuar
    continuar = input("¿Deseas realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        break
    