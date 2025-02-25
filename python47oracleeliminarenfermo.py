from conexionoracle47eliminarenfermos import ConexionOracleEnfermos

print("Probando clases de Oracle: ENFERMOS")
print("Introduzca una inscripción: Eliminar")
inscripcion = int(input())
#CREAMOS UN OBJETO CONNECTION PARA EJECUTAR LAS CONSULTAS
connection = ConexionOracleEnfermos()
eliminados = connection.eliminarEnfermo(inscripcion)
print(f"Enfermos eliminados: {eliminados}")
print("Fin de programa")