from class32mes import Mes

print("Trabajando con clase Mes")
enero = Mes()
enero.nombre = "Enero"
enero.temperaturaMaxima = 9
enero.temperaturaMinima = -4
media = enero.getTemperaturaMedia()
print("Enero ", media)
print(enero)
