# Programa para comparar las edades de tres personas

# Solicitar las edades
print("Comparacion de edades")
edad1 = int(input("Ingresa la edad de la primera persona: "))
edad2 = int(input("Ingresa la edad de la segunda persona: "))
edad3 = int(input("Ingresa la edad de la tercera persona: "))

# Mostrar las edades ingresadas
print("\nEdades ingresadas:")
print("Persona 1:", edad1, "años")
print("Persona 2:", edad2, "años")
print("Persona 3:", edad3, "años")

# Determinar quién es mayor, medio y menor
print("\n Resultados: ")

# Encontrar el mayor
if edad1 >= edad2 and edad1 >= edad3:
    mayor = edad1
    print("Mayor: Persona 1 con", mayor, "años")
elif edad2 >= edad1 and edad2 >= edad3:
    mayor = edad2
    print("Mayor: Persona 2 con", mayor, "años")
else:
    mayor = edad3
    print("Mayor: Persona 3 con", mayor, "años")

# Encontrar el menor
if edad1 <= edad2 and edad1 <= edad3:
    menor = edad1
    print("Menor: Persona 1 con", menor, "años")
elif edad2 <= edad1 and edad2 <= edad3:
    menor = edad2
    print("Menor: Persona 2 con", menor, "años")
else:
    menor = edad3
    print("Menor: Persona 3 con", menor, "años")

# Encontrar el del medio
if (edad1 >= edad2 and edad1 <= edad3) or (edad1 >= edad3 and edad1 <= edad2):
    medio = edad1
    print("Medio: Persona 1 con", medio, "años")
elif (edad2 >= edad1 and edad2 <= edad3) or (edad2 >= edad3 and edad2 <= edad1):
    medio = edad2
    print("Medio: Persona 2 con", medio, "años")
else:
    medio = edad3
    print("Medio: Persona 3 con", medio, "años")