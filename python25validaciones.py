from libreria25validaciones import validarISBN, validarDni

print("Clase Program validaciones")
print("Introduzca un número DNI")
numeroDni = int(input())
letra = validarDni(numeroDni)
print("Letra " + letra)
print("----------------")
print("Introduzca ISBN")
isbn=input()
valido = validarISBN(isbn)
print("El isbn es " , valido)