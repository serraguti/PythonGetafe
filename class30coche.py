class Coche:
    marca = ""
    modelo = ""
    velocidad = 0
    estado = False

    def getVelocidadMaxima(self):
        print("Velocidad máxima Coche: 140 km/h")
        return 140

    def acelerar(self):
        if (self.estado == False):
            print("El coche no está arrancado.  Debe arrancar antes")
        else:
            self.velocidad += 20
        print("Velocidad actual " + str(self.velocidad))
    
    def frenar(self):
        if (self.velocidad == 0):
            print("El coche está detenido")
        else:
            self.velocidad -= 10
        print("Velocidad actual " + str(self.velocidad))

    def arrancar(self):
        self.estado = True
        print("Coche arrancado")
    
    def detener(self):
        self.estado = False
        self.velocidad = 0
        print("Coche detenido")
