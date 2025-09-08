edad1 = int(input("Por favor, introduce la edad de la primera persona: "))

edad2 = int(input("Genial, ahora la edad de la segunda persona: "))

edad3 = int(input("Y por último, la edad de la tercera persona: "))

edades = [edad1, edad2, edad3]
edades.sort() # Se ordenan de mayor a menor

# Esto es para identificar por rango de edad
menor = edades[0]
medio = edades[1]
mayor = edades[2]


print(f"\n¡Listo! Aquí tienes el orden de las edades:")
print(f"La persona menor tiene {menor} años.")
print(f"La persona del medio tiene {medio} años.")
print(f"La persona mayor tiene {mayor} años.")
