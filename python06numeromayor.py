print("Número mayor dos números")
print("Introduzca número 1")
numero1 = int(input())
print("Introduzca número 2")
numero2 = int(input())
if (numero1 > numero2):
    print("El número " + str(numero1) + " es mayor que " + str(numero2))
elif (numero1 == numero2):
    print("Los dos números son iguales")
else:
    print("El número mayor es ", numero2)
print("Fin de programa")