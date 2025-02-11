print("Clase string y funciones")
texto = "primero python"
#VAMOS PROBANDO METODOS Y VIENDO QUE DEVUELVEN
print("upper ", texto.upper())
print("replace " + texto.replace("o", "@"))
print("Letra 0: " + texto[0])
print("Logitud (len)", len(texto))
print("find P: ", texto.find("p"))
print("find Z: ", texto.find("z"))
 # SOBRECARGA DE FIND (contenido a buscar, indice)
print("find p sobrecarga ", texto.find("p", 1))
print("rfind p ", texto.rfind("p"))
print("startswith A ", texto.startswith("A"))
print("endswith n ", texto.endswith("n"))
print("isdigit() ", texto.isdigit())
print("isalpha() ", texto.isalpha())
print("isalnum() ", texto.isalnum())
# Vamos a visualizar que pasa con SLICING
# SUBSTRING
# QUEREMOS RECUPERAR DESDE LA POSICION 2 EN ADELANTE
substring = texto[2:]
print("Posición 2 en adelante ", substring)
# EN PYTHON PODEMOS RECUPERAR UNA SUBCADENA
# DESDE UNA POSICION (2) A OTRA POSICION (5)
subtexto = texto[2: 5]
print("texto[2: 5] ", subtexto)
# PODEMOS RECORRER CADA CARACTER DE UN TEXTO
longitud = len(texto)
for i in range(longitud):
    letra = texto[i]
    print("Posición " + str(i) + ": " + letra)
# PODEMOS HASTA COMPROBAR QUE EL USUARIO HA ESCRITO NUMEROS O NO
print("Introduzca un número")
# PRIMERO A UNA VARIABLE AUXILIAR
aux = input()
if (aux.isdigit()):
    print("Esto es un número!!!")
else:
    print("No me has dado un número, campeón...")
print("Fin de programa")