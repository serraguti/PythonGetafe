def saludar(nombre):
    print("Bienvenido a Python Mr/Mrs " + nombre)

def despedirse(nombre, dia):
    print("Un placer hoy " + dia + " Mr/Mrs " + nombre)

# -----------------------------------------------------
print("Metodos con parametros")
name = "Alumno"
dia = "miercoles"
saludar(name)
despedirse("Jueves", dia)
print("Fin de programa")