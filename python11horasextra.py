print("Ejemplo Horas extra")
print("Horas trabajadas")
horasTrabajadas = int(input())
print("Precio hora")
precioHora = int(input())
print("Kilometros recorridos")
km = int(input())
horasExtra = 0
salarioExtra = 0
salarioBase = 0
salarioTotal = 0
dietas = ""
retencion = ""
#PREGUNTAMOS SI TENEMOS HORAS EXTRA
if (horasTrabajadas > 36):
    #HORAS EXTRA
    horasExtra = horasTrabajadas - 36
    salarioBase = precioHora * 36
    salarioExtra = horasExtra * (precioHora + 2)
else:
    #NO HA HECHO HORAS EXTRA
    horasExtra = 0
    salarioExtra = 0
    salarioBase = horasTrabajadas * precioHora
salarioTotal = salarioBase + salarioExtra
if (km <= 100):
    dietas = "LOCALES"
elif (km >= 101 and km <= 500):
    dietas = "PROVINCIALES"
else:
    dietas= "NACIONALES"
if (salarioTotal < 250):
    retencion = "SIN RETENCION"
elif (salarioTotal >= 250 and salarioTotal <= 600):
    retencion = "20% Retencion"
else:
    retencion = "40% Retención"
#INFORME
print("Informe de salario")
print("Horas trabajadas ", horasTrabajadas)
print("Horas extra ", horasExtra)
print("Precio hora ", precioHora)
print("Precio extra ", (precioHora + 2))
print("Salario base ", salarioBase)
print("Salario extra ", salarioExtra)
print("Salario total ", salarioTotal)
print("Retenciones ", retencion)
print("Dietas ", dietas)