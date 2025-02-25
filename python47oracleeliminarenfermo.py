from conexionoracle47eliminarenfermos import ConexionOracleEnfermos

print("Probando clases de Oracle: ENFERMOS")
print("Introduzca una inscripción: Update")
inscripcion = int(input())
print("Introduzca un Nuevo apellido")
apellido = input()
#CREAMOS UN OBJETO CONNECTION PARA EJECUTAR LAS CONSULTAS
connection = ConexionOracleEnfermos()
modificados = connection.modificarEnfermo(apellido, inscripcion)
print(f"Enfermos modificados: {modificados}")
print("Fin de programa")