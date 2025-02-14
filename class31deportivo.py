from class30coche import Coche

class Deportivo (Coche): 
    def getVelocidadMaxima(self):
        velocidadCoche = super().getVelocidadMaxima()
        return velocidadCoche + 100

    def acelerar(self):
        self.velocidad += 60
        print("Acelerando " + self.marca + " a " + str(self.velocidad) + " km/h")
    def turbo(self):
        self.velocidad += 120
        print("Velocidad actual: ", self.velocidad)
        print("Activando turbo!!!!")