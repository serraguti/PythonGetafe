from math import trunc
print("Dia nacimiento de la semana")
#LOS DATOS SON NUMEROS, DEBEMOS CONVERTIR
#LO QUE EL USUARIO ESTA ESCRIBIENDO
print("Introduzca día")
dia = int(input())
print("Introduzca mes")
mes = int(input())
print("Introduzca año")
anyo = int(input())
if (mes == 1):
    mes = 13
    anyo = anyo - 1
elif (mes == 2):
    mes = 14
    anyo = anyo - 1
op1 = trunc(((mes + 1) * 3) / 5)
op2 = trunc( anyo / 4)
op3 = trunc( anyo / 100)
op4 = trunc( anyo / 400)
# 5.	Sumar el dia, el doble del mes, el año
# , el resultado de la operación 1, el resultado de la operación 2
# , menos el resultado de la operación 3 más la operación 4 más 2.
op5 = trunc( dia + (mes * 2) + anyo + op1 + op2 - op3 + op4 + 2)
op6 = trunc(op5 / 7)
resultado = trunc( op5 - (op6 * 7))
diaSemana = ""
if (resultado == 0):
    diaSemana = "SABADO"
elif (resultado == 1):
    diaSemana = "DOMINGO"
elif (resultado == 2):
    diaSemana = "LUNES"
elif (resultado == 3):
    diaSemana = "MARTES"
elif (resultado == 4):
    diaSemana = "MIERCOLES"
elif (resultado == 5):
    diaSemana = "JUEVES"
elif (resultado == 6):
    diaSemana = "VIERNES"
print(diaSemana)
print("Fin de programa")