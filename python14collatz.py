print("Conjetura de Collatz")
print("Introduzca un número")
numero = int(input())
while (numero != 1):
    if (numero % 2 == 0):
        numero = int(numero / 2)
    else: 
        numero = numero * 3 + 1
    print(numero)
print("Fin de programa")