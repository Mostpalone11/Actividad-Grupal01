hombres = int(input("Ingrese la cantidad de hombres: "))
mujeres = int(int(input("Ingrese la cantidad de mujeres: ")))

total = hombres + mujeres

porcentaje_hombres = (hombres / total) * 100
porcentaje_mujeres = (mujeres / total) * 100

print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")

if abs(porcentaje_hombres - porcentaje_mujeres) <= 10:
    print("El grupo está equilibrado.")
else:
    print("El grupo no está equilibrado.")
