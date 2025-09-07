# Solicitar un número al usuario
numero = float(input("Ingresa un número: "))

# Determinar si es positivo, negativo o cero
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Determinar si es par o impar (solo para números enteros)
if numero % 1 == 0:  # Verificar si es un número entero
    numero_entero = int(numero)
    if numero_entero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
else:
    print("El número no es entero, por lo que no se puede determinar si es par o impar")