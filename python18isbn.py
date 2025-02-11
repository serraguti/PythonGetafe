print("Validar ISBN")
print("Introduzca un ISBN válido")
isbn = input()
longitud = len(isbn)
if (longitud != 10):
    print("El número ISBN debe tener 10 caracteres")
elif (isbn.isdigit() == False):
    print("El número ISBN debe contener solo números")
else:
    suma = 0
    for i in range(longitud):
        letra = isbn[i]
        numero = int(letra)
        operacion = numero * (i + 1)
        suma = suma + operacion
    if (suma % 11 == 0):
        print("El numero isbn " + isbn + " es CORRECTO")
    else:
        print("El número ISBN NO ES CORRECTO")
    print("Fin de programa")