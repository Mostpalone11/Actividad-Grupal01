mejor_dia = "viernes"

while True:
    dia = input("Ingresa un día de la semana: ").lower()  #Convertimos a minúsculas para evitar errores
    
    if dia == mejor_dia:
        print(f"Exelente! {mejor_dia.capitalize()} es el mejor día.")
        break
    else:
        print("No es el mejor día. Intenta de nuevo.")
