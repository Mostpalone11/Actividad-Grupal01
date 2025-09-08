numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")

# Usamos un ciclo for para multiplicar del 1 al 10
for i in range(1, 11):  # range(1, 11) genera los números del 1 al 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
