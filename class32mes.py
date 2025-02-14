class Mes:
    nombre = ""
    temperaturaMaxima = 0
    temperaturaMinima = 0

    def getTemperaturaMedia(self):
        return (self.temperaturaMaxima + self.temperaturaMinima) / 2
    
    def __str__(self):
        return self.nombre + ", Max: " + str(self.temperaturaMaxima) + ", Min: " + str(self.temperaturaMinima)