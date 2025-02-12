# DECLARACION METODOS
def sumarNumeros(num1, num2):
    return num1 + num2

def restarNumeros(num1, num2):
    return num1 - num2

def multiplicarNumeros(num1, num2):
    return num1 * num2

def mostrarMenu():
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("Seleccione una opción")

#--------------------------------
print("Calculadora metodos")
print("Introduzca numero 1")
numero1 = int(input())
print("Introduzca numero 2")
numero2 = int(input())
mostrarMenu()
opcion = int(input())
operacion = 0
if (opcion == 1):
    operacion = sumarNumeros(numero1, numero2)
elif (opcion == 2):
    operacion = restarNumeros(numero1, numero2)
elif (opcion == 3):
    operacion = multiplicarNumeros(numero1, numero2)
else:
    print("No ha seleccionado una opción correcta")
print("Operación " + str(operacion))
print("Fin de programa")