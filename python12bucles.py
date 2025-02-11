print("Ejemplo bucles")
print("For")
# NORMALMENTE LAS VARIABLES DE LOS BUCLES CONTADORES
# SE REPRESENTAN CON UNA SOLA LETRA (i, z, j)
for i in range(5):
    print("Valor de i ", i)
for i in range(1 , 6):
    print("Valor i: ", i)

print("WHILE")
# NECESITAMOS UNA VARIABLE PARA LA CONDICION DEL BUCLE
contador = 0
while (contador <= 5):
    # DEBEMOS INDICAR QUE SALDREMOS DEL BUCLE
    print("Contador ", contador)
    contador = contador + 1

print("Fin de programa")