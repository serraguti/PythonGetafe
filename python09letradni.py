print("Ejemplo letra DNI")
print("Introduzca numero DNI")
numeroDni = int(input())
#resultado = numeroDni - (int(numeroDni / 23) * 23)
resultado = numeroDni % 23
letra = ""
if (resultado == 0):
    letra = "T"
elif (resultado == 1):
    letra = "R"
elif (resultado == 2):
    letra = "W"
elif (resultado == 3):
    letra = "A"
elif (resultado == 4):
    letra = "G"
elif (resultado == 5):
    letra = "M"
elif (resultado == 6):
    letra = "Y"
elif (resultado == 7):
    letra = "F"
elif (resultado == 8):
    letra = "P"
elif (resultado == 9):
    letra = "D"
elif (resultado == 10):
    letra = "X"
elif (resultado == 11):
    letra = "B"
elif (resultado == 12):
    letra = "N"
elif (resultado == 13):
    letra = "J"
elif (resultado == 14):
    letra = "Z"
elif (resultado == 15):
    letra = "S"
elif (resultado == 16):
    letra = "Q"
elif (resultado == 17):
    letra = "V"
elif (resultado == 18):
    letra = "H"
elif (resultado == 19):
    letra = "L"
elif (resultado == 20):
    letra = "C"
elif (resultado == 21):
    letra = "K"
elif (resultado == 22):
    letra = "E"
elif (resultado == 23):
    letra = "T"
print("Letra " + letra)
print("Fin de programa")        