total_nomina = 0 

# Bucle para simular el cálculo de salario para 20 empleados
for i in range(1, 21):  
    
    salario_base_diario = 8 * 5  # 8 horas normales * $5/hora = $40
    salario_base_semanal = salario_base_diario * 6  # $40/día * 6 días = $240

    horas_extra_diarias = 2  # Horas extra trabajadas por día
    pago_hora_extra = 5  # Tarifa por hora extra

    salario_extra_diario = horas_extra_diarias * pago_hora_extra  # 2 horas * $5/hora = $10
    salario_extra_semanal = salario_extra_diario * 6  # $10/día * 6 días = $60

    salario_total_empleado = salario_base_semanal + salario_extra_semanal  # Salario base semanal + salario extra semanal

    #total a pagar por empleado
    print(f"Empleado {i}: Salario total a pagar = ${salario_total_empleado:.2f}") #muestra unicamente 2 decimales

    #total de la nómina
    total_nomina += salario_total_empleado

#total de la nómina
print(f"\nTotal de la nómina para los 20 empleados = ${total_nomina:.2f}") #mostrara unicamente 2 decimales

