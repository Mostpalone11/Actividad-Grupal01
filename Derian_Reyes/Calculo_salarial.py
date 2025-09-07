# Programa para calcular la nómina de 20 empleados

# Datos fijos
horas_normales_por_dia = 8
horas_extra_por_dia = 2
dias_trabajados = 6
pago_por_hora = 5.00
numero_empleados = 20

# Variables para acumular totales
total_nomina = 0

print("CÁLCULO DE NÓMINA")
print("Empleados:", numero_empleados)
print("Días trabajados por semana:", dias_trabajados)
print("Horas normales por día:", horas_normales_por_dia)
print("Horas extra por día:", horas_extra_por_dia)
print("Pago por hora: $", pago_por_hora)
print()

# Bucle para calcular el salario de cada empleado
for empleado in range(1, numero_empleados + 1):
    
    # Calcular horas normales y extras por semana
    horas_normales_semana = horas_normales_por_dia * dias_trabajados
    horas_extra_semana = horas_extra_por_dia * dias_trabajados
    
    # Calcular pagos
    pago_horas_normales = horas_normales_semana * pago_por_hora
    pago_horas_extra = horas_extra_semana * pago_por_hora * 1.5  # Las extras se pagan 50% más
    
    # Calcular salario total del empleado
    salario_empleado = pago_horas_normales + pago_horas_extra
    
    # Acumular al total de la nómina
    total_nomina = total_nomina + salario_empleado
    
    # Mostrar información del empleado
    print("Empleado", empleado)
    print("  Horas normales:", horas_normales_semana)
    print("  Horas extra:", horas_extra_semana)
    print("  Pago horas normales: $", pago_horas_normales)
    print("  Pago horas extra: $", pago_horas_extra)
    print("  Salario total: $", salario_empleado)
    print()

# Mostrar resumen final
print("RESUMEN FINAL")
print("Total de empleados:", numero_empleados)
print("Salario por empleado: $", salario_empleado)  # Todos ganan lo mismo
print("Total de la nómina: $", total_nomina)