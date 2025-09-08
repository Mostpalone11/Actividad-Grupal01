nombre = input("Ingrese el nombre del estudiante: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

#calcula el promedio
promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 6.0:
    print(f"El estudiante {nombre} ha aprobado con un promedio de {promedio:.2f}.")
else:
    print(f"El estudiante {nombre} ha reprobado con un promedio de {promedio:.2f}.")
