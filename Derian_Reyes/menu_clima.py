# Programa con menú interactivo

# Variable para controlar el bucle del menú
continuar = True

print("Menu interactivo")

# Bucle principal del menú
while continuar:
    
    # Mostrar opciones del menú
    print("\n Menu principal")
    print("1. Mostrar día de la semana")
    print("2. Recomendar actividad según clima")
    print("3. Salir")
    
    # Pedir opción al usuario
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    # Opción 1: Mostrar día de la semana
    if opcion == "1":
        print("\n Dia de la semana")
        numero_dia = int(input("Ingresa un número del 1 al 7: "))
        
        if numero_dia == 1:
            print("Día 1: Lunes")
        elif numero_dia == 2:
            print("Día 2: Martes")
        elif numero_dia == 3:
            print("Día 3: Miércoles")
        elif numero_dia == 4:
            print("Día 4: Jueves")
        elif numero_dia == 5:
            print("Día 5: Viernes")
        elif numero_dia == 6:
            print("Día 6: Sábado")
        elif numero_dia == 7:
            print("Día 7: Domingo")
        else:
            print("Error: Ingresa un número del 1 al 7")
    
    # Opción 2: Recomendar actividad según clima
    elif opcion == "2":
        print("\n Recomendacion de acividades")
        print("Tipos de clima disponibles:")
        print("- soleado")
        print("- lluvioso") 
        print("- nublado")
        print("- frio")
        
        clima = input("¿Cómo está el clima hoy?: ").lower()
        
        if clima == "soleado":
            print("Recomendación: ¡Perfecto para ir a la playa o hacer un picnic!")
        elif clima == "lluvioso":
            print("Recomendación: Mejor quédate en casa y lee un buen libro.")
        elif clima == "nublado":
            print("Recomendación: Ideal para caminar en el parque o ir de compras.")
        elif clima == "frio":
            print("Recomendación: Perfecto para tomar chocolate caliente y ver películas.")
        else:
            print("Clima no reconocido. Intenta con: soleado, lluvioso, nublado o frio")
    
    # Opción 3: Salir
    elif opcion == "3":
        print("\n¡Gracias por usar el programa!")
        print("¡Hasta luego!")
        continuar = False  # terminar el bucle
    
    # Opción inválida
    else:
        print("\nError: Opción no válida. Elige 1, 2 o 3.")

print("Programa terminado.")