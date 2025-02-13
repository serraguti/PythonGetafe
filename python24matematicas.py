# LOS IMPORT SE REALIZAN LO PRIMERO DE NUESTRO CODIGO
#from libreria24matematicas import sumarNumeros, restarNumeros, mostrarMenu
import libreria24matematicas

# CODIGO LOGIGO
print("Calculadora métodos")
numero1 = 9
numero2 = 19
libreria24matematicas.mostrarMenu()
opcion = int(input())
resultado = 0
if (opcion == 1):
    resultado = libreria24matematicas.sumarNumeros(numero1, numero2)
elif (opcion == 2):
    resultado = libreria24matematicas.restarNumeros(numero1, numero2)
elif (opcion == 3):
    resultado = libreria24matematicas.multiplicarNumeros(numero1, numero2)
else:
    print("No ha seleccionado una opción correcta")
print("Resultado ", resultado)
print("Fin de programa")