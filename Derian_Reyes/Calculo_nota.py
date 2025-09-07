# calculo de notas de un estudiante

# Solicitar datos del estudiante 
nombre = input("Ingresa tu nomnbre: ")

# solicitar las 3 notas

nota1 = float(input("ingrese la primera nota: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("ingrese la tercera nota: "))

# calcular el promedio 
Promedio = (nota1 + nota2 + nota3 ) / 3

# mostrar las notas y el promedio 
print("Resultado: ")
print("Estudiante:", nombre)
print("Nota 1: ", nota1)
print("Nota 2: ", nota2)
print("Nota 3: ", nota3)
print("Promedio: ", Promedio)

#Determinar si aprueba o no 

if Promedio >= 6:
    print("Aprobado")
    print("Felicidades", nombre + ", Has aprobado la materia!")

else:
    print("Reprobado")
    print("Lo siento", nombre + ", Has reprobado la materia.")
