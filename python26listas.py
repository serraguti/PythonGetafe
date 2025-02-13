print("Listas con Python")
listaNumeros = [12,56,77,88, 1,99,22]
# ORDEN ASCENDENTE
# listaNumeros.sort()
# Para ordenar de forma descendente debemos incluir
# dentro del método reverse = True
listaNumeros.sort(reverse = True)
# REALIZAMOS UN BUCLE PARA MOSTRAR LOS NUMEROS ACTUALMENTE
for i in range(len(listaNumeros)):
     print(listaNumeros[i])

# LAS LISTAS COMIENZAN EN CERO Y FINALIZAN EN LEN -1
print("Numero 0: ", listaNumeros[0])
print("Numero 1: ", listaNumeros[1])
listaNombres = ["Ana", "Lucas", "Adrian", "Diana", "Antonia", "Lucas"]
print("Nombre 2: ", listaNombres[2])
print("Nombre 4: ", listaNombres[4])
# append CREA UN NUEVO ELEMENTO EN LA LISTA AL FINAL
listaNombres.append("Lucia")
print("Nombre 5: ", listaNombres[5])
# insert() CREA UN ELEMENTO NUEVO EN UNA POSICION DE LA LISTA
listaNombres.insert(4, "Infiltrado")
# El metodo remove() elimina el primer objeto dentro de la lista
# si no lo encuentra da error
# listaNombres.remove("Lucas")
#listaNombres.pop(6)
# del listaNombres[0:4]
# clear() borra todo el contenido de una lista
# listaNombres.clear()
# Vamos a recorrer todos los elementos de la lista y mostrar
# su posición
# print("Dianis" in listaNombres)
# print("elementos")
listaNombres.sort()
for i in range(len(listaNombres)):
    print(str(i) + "=" + listaNombres[i])
