# Programa para calcular porcentajes de hombres y mujeres en un grupo

# Solicitar datos
hombres = int(input("Ingresa la cantidad de hombres: "))
mujeres = int(input("Ingresa la cantidad de mujeres: "))

# Calcular total de personas
total = hombres + mujeres

# Calcular porcentajes
porcentaje_hombres = (hombres * 100) / total
porcentaje_mujeres = (mujeres * 100) / total

# Calcular la diferencia entre porcentajes
diferencia = abs(porcentaje_hombres - porcentaje_mujeres)

# Mostrar resultados
print("RESULTADO")
print("Total de personas:", total)
print("Hombres:", hombres, "personas")
print("Mujeres:", mujeres, "personas")
print("Porcentaje de hombres:", porcentaje_hombres, "%")
print("Porcentaje de mujeres:", porcentaje_mujeres, "%")
print("Diferencia:", diferencia, "%")

# Determinar si el grupo está equilibrado
if diferencia <= 10:
    print("Estado: GRUPO EQUILIBRADO")
    print("El grupo esta balanceado.")
else:
    print("Estado: GRUPO NO EQUILIBRADO")
    print("El grupo tiene una diferencia mayor al 10%.")