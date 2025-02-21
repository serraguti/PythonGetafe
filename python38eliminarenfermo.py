import oracledb

print("Eliminar enfermo")
print("Introduzca inscripción para borrar")
data = input()
sql = "delete from ENFERMO where INSCRIPCION=" + data

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor  = connection.cursor()
#NO EXISTE DIFERENCIA, UN CURSOR EJECUTA CONSULTAS
#SI SON DE SELECCION, SE RECORREN
#SI SON DE ACCION, RECUPERAMOS SU int MEDIANTE rowcount
cursor.execute(sql)
afectados = cursor.rowcount
connection.commit()
print("Registros eliminados: " + str(afectados))
cursor.close()
connection.close()
print("Fin de programa BBDD")