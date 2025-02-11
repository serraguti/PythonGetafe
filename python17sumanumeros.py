print("Suma números texto string")
print("Introduzca un texto numérico")
textoNumeros = input()
suma = 0
longitud = len(textoNumeros)
# RECORREMOS CADA LETRA DEL TEXTO
for i in range(longitud):
    # ALMACENAMOS CADA LETRA DE CADA POSICION
    letra = textoNumeros[i]
    # CONVERTIMOS CADA LETRA A INTEGER
    numero = int(letra)
    # SUMAMOS CADA NUMERO
    suma = suma + numero
print("La suma de " + textoNumeros + " es " + str(suma))
print("Fin de programa")