while True:
    # Solicitar un día de la semana
    dia = input("Ingresa un día de la semana: ").lower().strip()
    
    # Verificar si es el mejor día (viernes)
    if dia == "viernes":
        print("¡Correcto! ¡Viernes es el mejor día! 🎉")
        break
    else:
        print(f"{dia.capitalize()} no es el mejor día. Intenta de nuevo")