from class29persona import Persona

print("Prueba clase Persona")
# CREAMOS UNA NUEVA PERSONA
person = Persona()
print(person.pais)
person.pais = "España"
person.anyonacimiento = 2000
person.email = "email@email.com"
person.nombre = "Alumno"
person.apellidos = "Python"
print(person.getDescripcion("Hola caracola"))
print(person.getNombreCompleto())
print("Edad : " ,person.getEdad())
person2 = Persona()
print(person2.pais)
print(person)
