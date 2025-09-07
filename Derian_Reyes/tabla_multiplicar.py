# Solicitar un número al usuario
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")
print("-" * 20)

# Mostrar la tabla del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")