print("Rango de números pares")
print("Introduzca un inicio")
inicio = int(input())
print("Introduzca un valor final")
fin = int(input())
# REALIZAMOS UN BUCLE DESDE UN INICIO HASTA UN FINAL + 1
for i in range(inicio, fin + 1):
    # PREGUNTAMOS SI EL NUMERO ES PAR
    if (i % 2 == 0):
        print(i)
print("Fin de programa")