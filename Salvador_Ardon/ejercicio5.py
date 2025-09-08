while True:
    print("\nMenú de opciones:")
    print("1. Mostrar día de la semana y recomendar actividad")
    print("2. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        # Pedir número de día
        num = int(input("Ingrese un número (1-7): "))
        dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

        if 1 <= num <= 7:
            print(f"El día es {dias[num-1]}")
            
            # Preguntar el clima
            clima = input("¿Cómo está el clima? (soleado/lluvioso/nublado): ").lower()
            
            if clima == "soleado":
                print("Recomendación: ¡Sal a la playa!")
            elif clima == "lluvioso":
                print("Recomendación: Ve una peli")
            elif clima == "nublado":
                print("Recomendación: Ve a Dormir")
            else:
                print("Clima no reconocido.")
        else:
            print("Número inválido.")

    elif opcion == "2":
        print("Saliendo del menú...")
        break
    else:
        print("Opción no válida.")
