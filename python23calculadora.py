# DECLARACION METODOS
def sumarNumeros(num1, num2):
    return num1 + num2

def restarNumeros(num1, num2):
    return num1 - num2

def multiplicarNumeros(num1, num2):
    return num1 * num2

def mostrarMenu():
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Introducir numeros de nuevo")
    print("Seleccione una opción")

def getNumeroComprobado():
    print("Introduzca numero")
    # ALMACENAR LO QUE HA ESCRITO EL USUARIO
    # EN UNA VARIABLE STRING
    aux = input()
    while (aux.isdigit() == False):
        print("Esto no es un numero")
        print("Introduzca numero")
        aux = input()           
    num = int(aux)
    return num
#--------------------------------
print("Calculadora metodos")
numero1 = getNumeroComprobado()
numero2 = getNumeroComprobado()
# ASIGNAMOS UN VALOR A OPCION PARA ENTRAR EN EL BUCLE
opcion = 1
# CREAMOS UN WHILE HASTA QUE EL USUARIO ESCRIBA 0
while (opcion != 0):
    mostrarMenu()
    opcion = int(input())
    operacion = 0
    if (opcion == 1):
        operacion = sumarNumeros(numero1, numero2)
    elif (opcion == 2):
        operacion = restarNumeros(numero1, numero2)
    elif (opcion == 3):
        operacion = multiplicarNumeros(numero1, numero2)
    elif (opcion == 4):
        # DEBEMOS PEDIR NUMEROS
        numero1 = getNumeroComprobado()
        numero2 = getNumeroComprobado()
    elif (opcion == 0):
        print("Hasta luego")
    else:
        print("No ha seleccionado una opción correcta")
    print("Operación " + str(operacion))
print("Fin de programa")









